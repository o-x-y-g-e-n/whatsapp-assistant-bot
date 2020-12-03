from configparser import ConfigParser
from os.path import dirname, abspath, join
def get_config_information():
    config = ConfigParser()    
    my_file = join(dirname(dirname(abspath(__file__))),"config.ini")
    config.read(my_file)
    return config.get('selenium','chromePath')

if(__name__ == '__main__'):
    print(get_config_information())