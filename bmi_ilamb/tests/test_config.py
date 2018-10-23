"""Unit tests for the bmi_ilamb.config.Configuration class."""

import os
import pytest

from ..config import Configuration
from .. import data_dir


bmi_ilamb_config = os.path.join(data_dir, 'bmi_ilamb.yaml')


def test_configuration_instantiates():
    x = Configuration()
    assert isinstance(x, Configuration)


def test_configuration_instantiates_with_filename():
    x = Configuration(bmi_ilamb_config)
    assert isinstance(x, Configuration)


def test_load_fails_with_no_argument():
    x = Configuration()
    with pytest.raises(TypeError):
        x.load()


def test_load_fails_with_nonexistent_file():
    x = Configuration()
    with pytest.raises(IOError):
        x.load('foo.txt')


def test_load():
    x = Configuration()
    x.load(bmi_ilamb_config)


def test_get_ilamb_root_returns_none_before_load():
    x = Configuration()
    r = x.get_ilamb_root()
    assert r is None


def test_get_ilamb_root():
    x = Configuration()
    x.load(bmi_ilamb_config)
    r = x.get_ilamb_root()
    assert type(r) is str


def test_set_model_root():
    x = Configuration()
    x.load(bmi_ilamb_config)
    x._set_model_root()
    r = x._config['model_root']
    assert os.path.isabs(r)


def test_get_arguments_returns_list_before_load():
    x = Configuration()
    r = x.get_arguments()
    assert type(r) is list


def test_get_arguments_omits_ilamb_root():
    x = Configuration()
    x.load(bmi_ilamb_config)
    r = x.get_arguments()
    assert r.count('ilamb_root') == 0


def test_get_arguments():
    x = Configuration()
    x.load(bmi_ilamb_config)
    r = x.get_arguments()
    assert len(r) == 4


def test_get_arguments_no_models():
    x = Configuration()
    x.load(bmi_ilamb_config)
    r = x.get_arguments()
    assert len(r) == 4


def test_get_arguments_with_models():
    x = Configuration()
    cfg = os.path.join(data_dir, 'bmi_ilamb_with_models.yaml')
    x.load(cfg)
    r = x.get_arguments()
    assert len(r) == 7


def test_get_arguments_no_confrontations():
    x = Configuration()
    x.load(bmi_ilamb_config)
    r = x.get_arguments()
    assert len(r) == 4


def test_get_arguments_with_confrontations():
    x = Configuration()
    cfg = os.path.join(data_dir, 'bmi_ilamb_with_confrontations.yaml')
    x.load(cfg)
    r = x.get_arguments()
    assert len(r) == 8


def test_get_arguments_no_regions():
    x = Configuration()
    x.load(bmi_ilamb_config)
    r = x.get_arguments()
    assert len(r) == 4


def test_get_arguments_with_regions1():
    x = Configuration()
    cfg = os.path.join(data_dir, 'bmi_ilamb_with_regions_1.yaml')
    x.load(cfg)
    r = x.get_arguments()
    assert len(r) == 6


def test_get_arguments_with_regions2():
    x = Configuration()
    cfg = os.path.join(data_dir, 'bmi_ilamb_with_regions_2.yaml')
    x.load(cfg)
    r = x.get_arguments()
    assert len(r) == 8


def test_get_arguments_no_build_dir():
    x = Configuration()
    x.load(bmi_ilamb_config)
    r = x.get_arguments()
    assert len(r) == 4


def test_get_arguments_with_build_dir():
    x = Configuration()
    cfg = os.path.join(data_dir, 'bmi_ilamb_with_build_dir.yaml')
    x.load(cfg)
    r = x.get_arguments()
    assert len(r) == 6


def test_get_arguments_no_user_regions():
    x = Configuration()
    x.load(bmi_ilamb_config)
    r = x.get_arguments()
    assert len(r) == 4


def test_get_arguments_with_netcdf_user_regions():
    x = Configuration()
    cfg = os.path.join(data_dir, 'bmi_ilamb_with_custom_regions_nc.yaml')
    x.load(cfg)
    r = x.get_arguments()
    assert len(r) == 10


def test_get_arguments_with_text_user_regions():
    x = Configuration()
    cfg = os.path.join(data_dir, 'bmi_ilamb_with_custom_regions_txt.yaml')
    x.load(cfg)
    r = x.get_arguments()
    assert len(r) == 8
