import docker
import imp 
import json
yaml_obj = imp.load_source('*', '../yaml/yaml_methods.py')

class DockerizeBaby:

    def __init__(self):

        self.cli = docker.from_env()
        self.yaml_worker = yaml_obj.ParseCompose()
        self.service_data = {}

    def connection (self):
        return self.cli.version    
    

    def get_service_data(self):
        return self.service_data



    def generate_container(self):
            for k, v in self.service_data.items():
                print(k  + "Service Elements : " + str(v))

                for i in v.keys():
                    ## i is the docker element 
                    ## v[i] is the value of the docker element
                    print("{}".format(i)+ "\t",v[i])
                            






    def set_service_data(self):
    
#            self.cli.containers.run(image="redis",detach=True)
     
        self.yaml_worker.read_file(path="/Users/emirozbir/Desktop/composepy/yaml/yml_test_files/docker-compose.yml")
        self.yaml_worker.set_services()

        service_data = self.yaml_worker.get_services()
        self.service_data = service_data

    def container_count(self):
        return len(self.cli.containers.list())


obj = DockerizeBaby()
obj.set_service_data()
print(obj.generate_container())
