"""Reads and parses a configuration file for the ILAMB BMI."""

from os.path import join
import yaml


ilamb_root_key = 'ilamb_root'
model_root_key = 'model_root'


class Configuration(object):

    def __init__(self):
        self._config = {}

    def load(self, filename):
        with open(filename, 'r') as fp:
            self._config = yaml.load(fp)

    def get_ilamb_root(self):
        return self._config.get(ilamb_root_key)

    def _set_model_root(self):
        rel = self._config.get(model_root_key)
        if rel is not None:
            self._config[model_root_key] = join(self.get_ilamb_root(), rel)

    def get_arguments(self):
        args = []
        self._set_model_root()
        for k, v in self._config.iteritems():
            if k != ilamb_root_key:
                args.append('--' + k)
                args.append(v)
        return args
