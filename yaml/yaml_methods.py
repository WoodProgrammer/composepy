import yaml

class ParseCompose:

    def __init__(self):

        
        self.main_data = {}
        self.services = {}
        self.service_keywords = {'environment','image','links','depends_on'}
    def get_services(self):
        return self.services
    
    def set_services(self):
        self.services = self.main_data['services']



    def read_file(self,path=None,key=None):
 
        with open("{}".format(path), 'r') as stream:
            try:
                yaml_data = yaml.load(stream)
                self.main_data = yaml_data
            except yaml.YAMLError as exc:
                print(exc)

        return self.main_data



