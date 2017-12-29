import yaml
def get_environ():
    pass
def read_file(key=None):

    with open("./yml_test_files/docker-compose.yml", 'r') as stream:
        try:
            yaml_data = yaml.load(stream)

            if key == None:
                return yaml_data
            else:
                return yaml_data[key]
        except yaml.YAMLError as exc:
            print(exc)





print(read_file(key='services'))