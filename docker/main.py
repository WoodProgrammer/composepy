import docker
import imp 
yaml_obj = imp.load_source('*', '../yaml/yaml_methods.py')

class DockerizeBaby:

    def __init__(self):

        self.cli = docker.from_env()
        self.yaml_worker = yaml_obj.ParseCompose()
        self.service_data = {}

    def connection (self):
        return self.cli.version    

    def create_container(self):
    
#            self.cli.containers.run(image="redis",detach=True)
        self.yaml_worker.read_file(path="/Users/emirozbir/Desktop/composepy/yaml/yml_test_files/docker-compose.yml")
        self.yaml_worker.set_services()

        self.service_data = self.yaml_worker.get_services()
        return self.service_data

    def container_count(self):
        return len(self.cli.containers.list())



