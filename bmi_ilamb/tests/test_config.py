"""Unit tests for the bmi_ilamb.config.Configuration class."""

import os
from nose.tools import (raises, assert_equal, assert_is, assert_true,
                        assert_is_instance, assert_is_none)
from ..config import Configuration
from .. import data_dir


bmi_ilamb_config = os.path.join(data_dir, 'bmi_ilamb.yaml')


def test_configuration_instantiates():
    x = Configuration()
    assert_is_instance(x, Configuration)


@raises(TypeError)
def test_load_fails_with_no_argument():
    x = Configuration()
    x.load()


@raises(IOError)
def test_load_fails_with_nonexistent_file():
    x = Configuration()
    x.load('foo.txt')


def test_load():
    x = Configuration()
    x.load(bmi_ilamb_config)


def test_get_ilamb_root_returns_none_before_load():
    x = Configuration()
    r = x.get_ilamb_root()
    assert_is_none(r)


def test_get_ilamb_root():
    x = Configuration()
    x.load(bmi_ilamb_config)
    r = x.get_ilamb_root()
    assert_is(type(r), str)


def test_set_model_root():
    x = Configuration()
    x.load(bmi_ilamb_config)
    x._set_model_root()
    r = x._config['model_root']
    assert_true(os.path.isabs(r))


def test_get_arguments_returns_list_before_load():
    x = Configuration()
    r = x.get_arguments()
    assert_is(type(r), list)


def test_get_arguments_omits_ilamb_root():
    x = Configuration()
    x.load(bmi_ilamb_config)
    r = x.get_arguments()
    assert_equal(r.count('ilamb_root'), 0)


def test_get_arguments():
    x = Configuration()
    x.load(bmi_ilamb_config)
    r = x.get_arguments()
    assert_equal(len(r), 6)


def test_get_arguments_no_models():
    x = Configuration()
    x.load(bmi_ilamb_config)
    r = x.get_arguments()
    assert_equal(len(r), 6)


def test_get_arguments_with_models():
    x = Configuration()
    cfg = os.path.join(data_dir, 'bmi_ilamb_with_models.yaml')
    x.load(cfg)
    r = x.get_arguments()
    assert_equal(len(r), 8)


def test_get_arguments_no_confrontations():
    x = Configuration()
    x.load(bmi_ilamb_config)
    r = x.get_arguments()
    assert_equal(len(r), 6)


def test_get_arguments_with_confrontations():
    x = Configuration()
    cfg = os.path.join(data_dir, 'bmi_ilamb_with_confrontations.yaml')
    x.load(cfg)
    r = x.get_arguments()
    assert_equal(len(r), 10)
