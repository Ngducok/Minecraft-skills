import json
import unittest
import xml.etree.ElementTree as ET
from tools.cli import ROOT, read


class Examples(unittest.TestCase):
    def test_pack_formats_match_exact_release(self):
        release=next(x for x in read(ROOT/'knowledge/minecraft/versions/matrix.json')['releases'] if x['minecraft']=='1.21.11')
        for folder,key in [('datapack','data_pack'),('resourcepack','resource_pack')]:
            metadata=read(ROOT/f'examples/{folder}/pack.mcmeta')['pack']
            self.assertEqual(metadata['min_format'],release[key])
            self.assertEqual(metadata['max_format'],release[key])
            self.assertNotIn('supported_formats',metadata)

    def test_datapack_load_references_existing_function(self):
        tag=read(ROOT/'examples/datapack/data/minecraft/tags/function/load.json')
        for value in tag['values']:
            namespace,name=value.split(':')
            self.assertTrue((ROOT/f'examples/datapack/data/{namespace}/function/{name}.mcfunction').is_file())

    def test_translation_and_paper_dependency_scope(self):
        self.assertEqual(read(ROOT/'examples/resourcepack/assets/agentcheck/lang/en_us.json')['agentcheck.status'],'Agent resource pack active')
        pom=ET.parse(ROOT/'examples/paper-plugin/pom.xml')
        ns={'m':'http://maven.apache.org/POM/4.0.0'}
        dependency=pom.find('.//m:dependency',ns)
        self.assertEqual(dependency.find('m:scope',ns).text,'provided')
        self.assertEqual(dependency.find('m:version',ns).text,'1.21.11-R0.1-SNAPSHOT')


if __name__=='__main__':
    unittest.main()
