import configparser
import os
import sys
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    def __init__(self, name):
        self.name = name
        self.config = self.read_ini()[name]
        pass

    def read_ini(self):
        config_file_name = os.environ.get("config-file", "project-config.ini")
        root_path = os.path.join(sys.path[0], '../..', config_file_name)
        parser = configparser.ConfigParser()
        parser.read(root_path)
        return parser

    def __getattr__(self, item):
        return os.environ.get(item.upper(), self.config[item])
