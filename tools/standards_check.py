"""Optional standards validator used by CI, not required by offline CLI."""
import jsonschema
import yaml
from .cli import ROOT, read, validate


def main():
    validate(ROOT)
    schemas={name:read(ROOT/f'schemas/{name}.schema.json') for name in ('skill','project','compatibility')}
    for schema in schemas.values():
        jsonschema.Draft202012Validator.check_schema(schema)
    for path in (ROOT/'skills').rglob('contract.json'):
        jsonschema.validate(read(path),schemas['skill'])
        text=(path.parent/'SKILL.md').read_text(encoding='utf-8')
        metadata=yaml.safe_load(text.split('---',2)[1])
        if metadata['name']!=path.parent.name or not 1<=len(metadata['description'])<=1024:
            raise ValueError(f'{path}: invalid Agent Skills metadata')
    for path in (ROOT/'examples').rglob('project*.json'):
        jsonschema.validate(read(path),schemas['project'])
    jsonschema.validate(read(ROOT/'knowledge/minecraft/versions/matrix.json'),schemas['compatibility'])
    for kind,schema_name in [('project','project'),('contract','skill')]:
        jsonschema.validate(read(ROOT/f'tests/fixtures/valid/{kind}.json'),schemas[schema_name])
        try:
            jsonschema.validate(read(ROOT/f'tests/fixtures/invalid/{kind}.json'),schemas[schema_name])
        except jsonschema.ValidationError:
            pass
        else:
            raise ValueError(f'Invalid fixture accepted: {kind}')
    print('PASS: Draft 2020-12 schemas, data and YAML frontmatter; negative fixtures rejected.')


if __name__=='__main__':
    main()
