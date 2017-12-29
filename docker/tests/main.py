import docker 
class DockerizeBaby:

    def __init__(self):

        self.cli = docker.from_env()

    def connection (self):
        return self.cli.version    

    def create_container(self):
        try:

            self.cli.containers.run(image="redis",detach=True)
            return True
        except:
            return False


    def container_count(self):
        return len(self.cli.containers.list())