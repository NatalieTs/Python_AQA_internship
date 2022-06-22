import configparser
import os
import sys


class Config(object):
    def __init__(self, name):
        self.name = name
        self.config = self.read_ini()[name]
        pass

    def read_ini(self):
        config_file_path = os.path.join(sys.path[0], '../..', "project-config.ini")
        parser = configparser.ConfigParser()
        parser.read("project-config.ini")
        parser.read(config_file_path)
        return parser

    def __getattr__(self, item):
        return self.config[item]

