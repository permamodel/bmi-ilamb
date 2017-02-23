"""Reads and parses a configuration file for the ILAMB BMI."""

from os.path import join
import yaml


ilamb_root_key = 'ilamb_root'
model_root_key = 'model_root'
models_key = 'models'
confrontations_key = 'confrontations'


class Configuration(object):

    def __init__(self, filename=None):
        self._config = {}
        if filename is not None:
            self.load(filename)

    def load(self, filename):
        with open(filename, 'r') as fp:
            self._config = yaml.load(fp)

    def get_ilamb_root(self):
        return self._config.get(ilamb_root_key)

    def _set_model_root(self):
        rel = self._config.get(model_root_key)
        if rel is not None:
            self._config[model_root_key] = join(self.get_ilamb_root(), rel)

    def _deserialize_models(self):
        models = self._config.get(models_key)
        if models is not None:
            self._config[models_key] = ' '.join(models)

    def _deserialize_confrontations(self):
        clash = self._config.get(confrontations_key)
        if clash is not None:
            self._config[confrontations_key] = ' '.join(clash)

    def get_arguments(self):
        args = []
        self._set_model_root()
        self._deserialize_models()
        self._deserialize_confrontations()
        for k, v in self._config.iteritems():
            if (k != ilamb_root_key) and (v is not None):
                args.append('--' + k)
                args.append(v)
        return args
