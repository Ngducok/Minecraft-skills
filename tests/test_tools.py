import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.cli import ROOT, read, resolve, route, schema_check, validate, inside


class Contracts(unittest.TestCase):
    def setUp(self):
        self.context=read(ROOT/'examples/project.json')

    def test_repository(self):
        self.assertGreaterEqual(validate(ROOT),62)

    def test_valid_and_invalid_contracts(self):
        schema=read(ROOT/'schemas/skill.schema.json')
        schema_check(read(ROOT/'tests/fixtures/valid/contract.json'),schema)
        with self.assertRaises(ValueError):
            schema_check(read(ROOT/'tests/fixtures/invalid/contract.json'),schema)

    def test_context_rejects_wrong_types_extra_fields_and_bool_java(self):
        schema=read(ROOT/'schemas/project.schema.json')
        for changes in ({'java':'21'},{'java':True},{'edition':'unknown'},{'resource_pack':[75]},{'token':'secret'}):
            with self.subTest(changes=changes),self.assertRaises(ValueError):
                schema_check(self.context|changes,schema)

    def test_unknown_versions_do_not_fall_back(self):
        for version in ('1.21.10','1.20.4','latest','26.1'):
            self.assertEqual(resolve(self.context|{'minecraft':version},ROOT)['status'],'unknown')

    def test_missing_context_stays_unresolved(self):
        result=resolve(read(ROOT/'examples/project-unresolved.json'),ROOT)
        self.assertEqual(result['status'],'needs-context')
        self.assertIn('minecraft',result['missing'])

    def test_formats_and_java_have_separate_evidence(self):
        documented=resolve(self.context,ROOT)
        self.assertEqual(documented['status'],'documented')
        self.assertFalse(documented['api_verified'])
        self.assertEqual(documented['release']['data_pack'],[94,1])
        for changes in ({'java':17},{'java':None},{'resource_pack':[69,0]},{'data_pack':[75,0]},{'platform':'forge'}):
            with self.subTest(changes=changes):
                self.assertEqual(resolve(self.context|changes,ROOT)['status'],'needs-verification')

    def test_spigot_cannot_route_paper_dialog(self):
        result=route('custom dialog item',self.context|{'platform':'spigot'},ROOT)
        names=[x['name'] for x in result['selected']]
        self.assertIn('minecraft-spigot-plugin',names)
        self.assertNotIn('minecraft-dialog-ui',names)
        self.assertIn('minecraft-dialog-ui',[x['name'] for x in result['excluded']])

    def test_farming_is_not_default(self):
        self.assertNotIn('minecraft-farming',[x['name'] for x in route('command permission',self.context,ROOT)['selected']])
        self.assertIn('minecraft-farming',[x['name'] for x in route('farm growth',self.context,ROOT)['selected']])

    def test_bedrock_not_routed_to_java_content(self):
        context=self.context|{'edition':'bedrock','platform':'bedrock','java':None}
        names=[x['name'] for x in route('dialog custom item pack',context,ROOT)['selected']]
        self.assertIn('minecraft-bedrock-addons',names)
        self.assertNotIn('minecraft-dialog-ui',names)
        self.assertNotIn('minecraft-item-models',names)

    def test_path_escape_and_schema_extension_rejected(self):
        with self.assertRaises(ValueError):
            inside(ROOT,ROOT/'../outside')
        with self.assertRaises(ValueError):
            schema_check({}, {'type':'object','unimplementedKeyword':True})

    def test_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as temp:
            path=Path(temp)/'project.json'
            for context,code in [(self.context,0),(self.context|{'minecraft':'latest'},2),(self.context|{'java':'21'},1)]:
                path.write_text(json.dumps(context),encoding='utf-8')
                result=subprocess.run([sys.executable,'-m','tools.cli','resolve',str(path)],cwd=ROOT,capture_output=True,timeout=20)
                self.assertEqual(result.returncode,code,result.stderr)

    def test_catalog_is_deterministic(self):
        from tools.cli import catalog
        self.assertEqual(catalog(ROOT),read(ROOT/'catalog.json'))
        self.assertEqual(catalog(ROOT),catalog(ROOT))


class MCP(unittest.TestCase):
    def exchange(self,requests):
        data='\n'.join(json.dumps(x) for x in requests)+'\n'
        process=subprocess.run([sys.executable,'-m','tools.mcp_server'],cwd=ROOT,input=data,text=True,capture_output=True,timeout=30)
        self.assertEqual(process.returncode,0,process.stderr)
        return [json.loads(x) for x in process.stdout.splitlines()]

    def test_initialize_tools_read_and_traversal(self):
        rows=self.exchange([
            {'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2025-06-18','capabilities':{},'clientInfo':{'name':'test','version':'1'}}},
            {'jsonrpc':'2.0','method':'notifications/initialized'},
            {'jsonrpc':'2.0','id':2,'method':'tools/list'},
            {'jsonrpc':'2.0','id':3,'method':'tools/call','params':{'name':'skill','arguments':{'name':'minecraft-evidence','document':'SKILL.md'}}},
            {'jsonrpc':'2.0','id':4,'method':'tools/call','params':{'name':'skill','arguments':{'name':'../secrets','document':'SKILL.md'}}},
            {'jsonrpc':'2.0','id':5,'method':'tools/call','params':{'name':'resolve','arguments':{'context':read(ROOT/'examples/project.json')}}},
        ])
        self.assertEqual(len(rows),5)
        self.assertEqual(rows[0]['result']['protocolVersion'],'2025-06-18')
        self.assertEqual(len(rows[1]['result']['tools']),3)
        self.assertIn('minecraft-evidence',rows[2]['result']['content'][0]['text'])
        self.assertTrue(rows[3]['result']['isError'])
        self.assertEqual(json.loads(rows[4]['result']['content'][0]['text'])['status'],'documented')

    def test_lifecycle_and_unknown_methods(self):
        rows=self.exchange([{'jsonrpc':'2.0','id':1,'method':'tools/list'},
                            {'jsonrpc':'2.0','id':2,'method':'initialize','params':{'protocolVersion':'unknown'}},
                            {'jsonrpc':'2.0','method':'notifications/initialized'},
                            {'jsonrpc':'2.0','id':3,'method':'unknown'}])
        self.assertIn('error',rows[0])
        self.assertEqual(rows[1]['result']['protocolVersion'],'2025-06-18')
        self.assertEqual(rows[2]['error']['code'],-32601)


if __name__=='__main__':
    unittest.main()
