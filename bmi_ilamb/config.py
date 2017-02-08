"""Reads and parses a configuration file for the ILAMB BMI."""

import yaml


ilamb_root_key = 'ilamb_root'


class Configuration(object):

    def __init__(self):
        self._config = {}

    def load(self, filename):
        with open(filename, 'r') as fp:
            self._config = yaml.load(fp)

    def get_ilamb_root(self):
        return self._config.get(ilamb_root_key)

    def get_arguments(self):
        args = []
        for k, v in self._config.iteritems():
            if k != ilamb_root_key:
                args.append('--' + k)
                args.append(v)
        return args
