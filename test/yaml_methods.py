import yaml

class ParseCompose:

    def __init__(self):

        
        self.main_data = {}
        self.services = {}
        self.service_keywords = {'environment','image','links','depends_on'}
    def create_service_datas(self):
        pass




    def get_environ(self):
        pass
        
        

    def read_file(self,key=None):

        with open("./yml_test_files/docker-compose.yml", 'r') as stream:
            try:
                yaml_data = yaml.load(stream)
                self.main_data = yaml_data
            except yaml.YAMLError as exc:
                print(exc)


obj = ParseCompose()
obj.read_file()
print(obj.get_environ())


