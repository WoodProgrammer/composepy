import unittest
from yaml_methods import ParseCompose

class TestYaml(unittest.TestCase):

    #def test_read_file(self):
     #   self.assertTrue(read_file())

    #def test_services_key(self):
     #   self.assertTrue(read_file(key="services"))

    def test_services_key(self):
        obj = ParseCompose()

        obj.read_file()
        obj.set_services()

        test_dict = {'web': {'build': '.', 'ports': ['5000:5000']}, 'redis': {'image': 'redis:alpine'}}
        self.assertDictEqual(test_dict,obj.get_services())

if __name__ == '__main__':
    unittest.main()