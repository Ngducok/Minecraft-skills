"""Offline CLI. Validates the repository's explicitly bounded JSON Schema profile."""
import argparse
import json
import re
import sys
import unittest
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
KEYWORDS = {
    '$schema', '$id', 'title', 'description', 'type', 'enum', 'properties',
    'required', 'additionalProperties', 'items', 'minItems', 'maxItems',
    'minimum', 'maximum', 'minLength', 'maxLength', 'pattern', 'uniqueItems',
}
TYPES = {'object': dict, 'array': list, 'string': str, 'integer': int,
         'number': (int, float), 'boolean': bool, 'null': type(None)}


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def schema_check(value, schema, where='$'):
    """Fail closed on unsupported schema keywords; not a general Draft validator."""
    unknown = set(schema) - KEYWORDS
    if unknown:
        raise ValueError(f'{where}: unsupported schema keywords {sorted(unknown)}')
    kinds = schema.get('type', list(TYPES))
    if isinstance(kinds, str):
        kinds = [kinds]
    if any(kind not in TYPES for kind in kinds):
        raise ValueError(f'{where}: unsupported type')
    if not any(isinstance(value, TYPES[k]) and not
               (isinstance(value, bool) and k in ('integer', 'number')) for k in kinds):
        raise ValueError(f'{where}: expected {kinds}')
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError(f'{where}: outside enum')
    if isinstance(value, dict):
        missing = set(schema.get('required', [])) - value.keys()
        if missing:
            raise ValueError(f'{where}: missing {sorted(missing)}')
        props = schema.get('properties', {})
        for key, item in value.items():
            if key in props:
                schema_check(item, props[key], f'{where}.{key}')
            elif schema.get('additionalProperties') is False:
                raise ValueError(f'{where}: unknown property {key}')
    if isinstance(value, list):
        if len(value) < schema.get('minItems', 0) or len(value) > schema.get('maxItems', sys.maxsize):
            raise ValueError(f'{where}: array length')
        if schema.get('uniqueItems') and len({json.dumps(x, sort_keys=True) for x in value}) != len(value):
            raise ValueError(f'{where}: duplicate items')
        for i, item in enumerate(value):
            if 'items' in schema:
                schema_check(item, schema['items'], f'{where}[{i}]')
    if isinstance(value, str):
        if len(value) < schema.get('minLength', 0) or len(value) > schema.get('maxLength', sys.maxsize):
            raise ValueError(f'{where}: string length')
        if 'pattern' in schema and not re.search(schema['pattern'], value):
            raise ValueError(f'{where}: pattern mismatch')
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if value < schema.get('minimum', -float('inf')) or value > schema.get('maximum', float('inf')):
            raise ValueError(f'{where}: numeric bounds')


def inside(root, path):
    path = path.resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f'Path escapes repository: {path.name}')
    return path


def catalog(root):
    rows = []
    for path in sorted((root / 'skills').rglob('contract.json')):
        inside(root, path)
        item = read(path)
        rows.append({key: item[key] for key in ('name', 'category', 'description')} |
                    {'path': path.parent.relative_to(root).as_posix()})
    return {'schema_version': 1, 'skills': sorted(rows, key=lambda x: x['name'])}


def validate(root):
    skill_schema = read(root / 'schemas/skill.schema.json')
    sources = read(root / 'knowledge/sources.json')
    for key, source in sources.items():
        url = urlparse(source['url'])
        if url.scheme != 'https' or not url.netloc:
            raise ValueError(f'{key}: source needs HTTPS URL')
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', source['checked']):
            raise ValueError(f'{key}: inspection date missing')
        if source['status'] != 'inspected':
            raise ValueError(f'{key}: unsupported source status')
    found = catalog(root)
    if not found['skills']:
        raise ValueError('No skills found')
    seen = set()
    for row in found['skills']:
        folder = inside(root, root / row['path'])
        contract = read(folder / 'contract.json')
        schema_check(contract, skill_schema, row['name'])
        if folder.name != contract['name'] or contract['name'] in seen:
            raise ValueError(f'{folder.name}: name mismatch or duplicate')
        if folder.parent.relative_to(root / 'skills').as_posix() != contract['category']:
            raise ValueError(f'{folder.name}: category mismatch')
        seen.add(contract['name'])
        text = (folder / 'SKILL.md').read_text(encoding='utf-8')
        front = re.match(r'---\nname: ([a-z0-9-]+)\ndescription: ("[^\n]+")\n---\n', text)
        if not front or front[1] != contract['name'] or json.loads(front[2]) != contract['description']:
            raise ValueError(f'{folder.name}: invalid canonical frontmatter')
        for key in contract['sources']:
            if key not in sources:
                raise ValueError(f'{folder.name}: unknown source {key}')
        for required in ('REFERENCE.md', 'examples/request.md', 'tests/scenario.json'):
            if not (folder / required).is_file():
                raise ValueError(f'{folder.name}: missing {required}')
        scenario = read(folder / 'tests/scenario.json')
        if scenario['skill'] != contract['name'] or not scenario['prompt'] or not scenario['expected']:
            raise ValueError(f'{folder.name}: invalid behavioral scenario')
    if read(root / 'catalog.json') != found:
        raise ValueError('Catalog stale: run index')
    if {p.parent.resolve() for p in (root / 'skills').rglob('SKILL.md')} != {
            (root / row['path']).resolve() for row in found['skills']}:
        raise ValueError('Missing contract or SKILL.md')
    for path in (root / 'skills').rglob('*.md'):
        for target in re.findall(r'\]\(([^\s)]+)\)', path.read_text(encoding='utf-8')):
            if target.startswith(('https://', 'http://', '#')):
                continue
            target = target.split('#', 1)[0]
            if not inside(root, path.parent / target).exists():
                raise ValueError(f'{path.relative_to(root)}: broken link {target}')
    matrix = read(root / 'knowledge/minecraft/versions/matrix.json')
    schema_check(matrix, read(root / 'schemas/compatibility.schema.json'))
    targets = set()
    for row in matrix['releases']:
        key = row['edition'], row['minecraft']
        if key in targets or row['source'] not in sources:
            raise ValueError(f'{key}: duplicate target or unknown provenance')
        targets.add(key)
        for platform in row['platforms']:
            if platform['source'] not in sources:
                raise ValueError(f'{key}: unknown platform source')
        # ponytail: matrix currently documents facts only; add evidence artifacts before testing claims.
        if row['verification'] != 'documented' or any(row[k] for k in ('compile_tested','runtime_tested','client_tested')):
            raise ValueError(f'{key}: test claim needs evidence artifact support')
    for row in found['skills']:
        if read(root / row['path'] / 'contract.json')['supports']['verified_versions']:
            raise ValueError(f'{row["name"]}: verified release requires evidence artifacts')
    return len(seen)


def resolve(context, root):
    schema_check(context, read(root / 'schemas/project.schema.json'))
    missing = [key for key in ('edition', 'minecraft', 'platform') if context[key] is None]
    if missing:
        return {'status':'needs-context', 'missing':missing}
    matrix = read(root / 'knowledge/minecraft/versions/matrix.json')
    row = next((x for x in matrix['releases'] if (x['edition'],x['minecraft']) ==
                (context['edition'],context['minecraft'])), None)
    if row is None:
        return {'status':'unknown', 'reason':'No exact release evidence; inspect official target sources.'}
    platforms = [p for p in row['platforms'] if p['name'] == context['platform']]
    errors = []
    if not platforms and context['platform'] != 'vanilla':
        errors.append('Platform/toolchain compatibility not recorded.')
    if platforms and context['java'] is None:
        errors.append('Java runtime unresolved.')
    elif platforms and context['java'] < platforms[0]['java_recommended']:
        errors.append('Java below documented recommendation; verify target requirements.')
    for key, field in (('resource_pack','resource_pack'),('data_pack','data_pack')):
        if context.get(key) is not None and context[key] != row[field]:
            errors.append(f'{key}: requested format differs from exact release format; inspect compatibility range.')
    return {'status':'needs-verification' if errors else 'documented', 'issues':errors,
            'release':row, 'api_verified':False,
            'next':'Pin platform build/dependencies, inspect symbols/formats, then build and runtime/client test as needed.'}


ROUTES = {
    'dialog': ['minecraft-dialog-ui','minecraft-menu-ux','minecraft-bitmap-fonts'],
    'inventory': ['minecraft-inventory-ui','minecraft-inventory-transactions'],
    'item': ['minecraft-items-equipment','minecraft-item-models'],
    'pack': ['minecraft-pack-delivery'],
    'economy': ['minecraft-economy'], 'farm': ['minecraft-farming'],
    'quest': ['minecraft-quests'], 'combat': ['minecraft-combat-rules'],
    'world': ['minecraft-world-generation','minecraft-map-design'],
    'schematic': ['minecraft-schematics'], 'test': ['minecraft-testing'],
    'deploy': ['minecraft-release-recovery'], 'performance':['minecraft-performance'],
    'command': ['minecraft-commands-permissions'], 'datapack':['minecraft-datapacks'],
    'subagent':['minecraft-subagents'], 'handoff':['minecraft-coworker'],
}
PLATFORM_SKILLS = {p:'minecraft-'+p+'-'+('mod' if p in ('fabric','forge','neoforge') else 'plugin')
                   for p in ('paper','purpur','spigot','velocity','fabric','forge','neoforge')}


def route(task, context, root):
    schema_check(context, read(root / 'schemas/project.schema.json'))
    names = ['minecraft-project-context','minecraft-evidence']
    if context['platform'] in PLATFORM_SKILLS:
        names.append(PLATFORM_SKILLS[context['platform']])
    if context['platform'] == 'folia':
        names.append('minecraft-scheduling')
    if context['edition'] == 'bedrock':
        names.append('minecraft-bedrock-addons')
    for keyword, candidates in ROUTES.items():
        if re.search(r'\b'+keyword+r'\w*\b',task.lower()):
            names.extend(candidates)
    by_name = {x['name']:x for x in catalog(root)['skills']}
    selected, excluded = [], []
    for name in dict.fromkeys(names):
        row = by_name.get(name)
        if row is None:
            raise ValueError(f'Router references missing skill: {name}')
        support = read(root / row['path'] / 'contract.json')['supports']
        if context['edition'] and context['edition'] not in support['editions']:
            excluded.append({'name':name,'reason':'edition mismatch'})
        elif support['platforms'] and context['platform'] and context['platform'] not in support['platforms']:
            excluded.append({'name':name,'reason':'platform mismatch; research an alternative'})
        else:
            selected.append(row)
    return {'selected':selected,'excluded':excluded,'compatibility':resolve(context,root),
            'note':'Keyword routing is advisory. Read contracts and task semantics; it cannot certify compatibility.'}


def main(argv=None):
    parser = argparse.ArgumentParser(prog='minecraft-skills')
    parser.add_argument('--root',type=Path,default=ROOT,help='Explicit repository checkout when installed CLI is elsewhere')
    commands = parser.add_subparsers(dest='command',required=True)
    for name in ('validate','lint','index','test'):
        commands.add_parser(name)
    version = commands.add_parser('resolve')
    version.add_argument('context',type=Path)
    routing = commands.add_parser('route')
    routing.add_argument('context',type=Path)
    routing.add_argument('task')
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        if args.command in ('validate','lint'):
            print(f'PASS: {validate(root)} skill contracts, local references and provenance. Offline; no live links/build/client verification.')
        elif args.command == 'index':
            (root / 'catalog.json').write_text(json.dumps(catalog(root),indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
        elif args.command == 'test':
            suite = unittest.defaultTestLoader.discover(str(root / 'tests'),pattern='test_*.py',top_level_dir=str(root))
            if suite.countTestCases() == 0:
                raise ValueError('No tests discovered')
            return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1
        else:
            result = resolve(read(args.context),root) if args.command == 'resolve' else route(args.task,read(args.context),root)
            print(json.dumps(result,indent=2))
            if args.command == 'resolve' and result['status'] != 'documented':
                return 2
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(f'ERROR: {error}',file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
