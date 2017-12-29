import unittest
from main import *
class TestDockerMethods(unittest.TestCase):

    def test_connection(self):
        self.assertTrue(connection())

    def test_container_creation(self):
        self.assertTrue(create_container())

            
    def test_container_count(self):      
        self.assertEqual(3,container_count())

if __name__ == '__main__':
    unittest.main()
