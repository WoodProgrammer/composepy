import unittest
import imp 
from main import DockerizeBaby

obj = DockerizeBaby()
class TestDockerMethods(unittest.TestCase):

    def test_connection(self):
        self.assertTrue(obj.connection())

    def test_container_creation(self):
        self.assertTrue(obj.create_container())

            
    #def test_container_count(self):      
     #   self.assertEqual(3,obj.container_count())


    def test_insertion(self):      
        self.assertTrue(obj.create_container())
    



if __name__ == '__main__':
    unittest.main()
