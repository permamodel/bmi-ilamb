"""Unit tests for the ILAMB BMI."""

import os
from nose.tools import raises, assert_is, assert_equal, assert_true
from bmi_ilamb import BmiIlamb
from . import ilamb_is_installed
from .. import data_dir


bmi_ilamb_config = os.path.join(data_dir, 'bmi_ilamb.yaml')


def test_component_name():
    component = BmiIlamb()
    name = component.get_component_name()
    assert_equal(name, 'ILAMB')
    assert_is(component.get_component_name(), name)


def test_start_time():
    component = BmiIlamb()
    assert_equal(component.get_start_time(), 0.0)


def test_end_time():
    component = BmiIlamb()
    assert_equal(component.get_end_time(), 1.0)


def test_current_time():
    component = BmiIlamb()
    assert_equal(component.get_current_time(), 0.0)


def test_time_step():
    component = BmiIlamb()
    assert_equal(component.get_time_step(), 1.0)


def test_time_units():
    component = BmiIlamb()
    assert_equal(component.get_time_units(), 's')


def test_get_input_var_names():
    component = BmiIlamb()
    assert_equal(component.get_input_var_names(), ())


def test_get_output_var_names():
    component = BmiIlamb()
    assert_equal(component.get_output_var_names(), ())


@raises(TypeError)
def test_initialize_no_argument():
    component = BmiIlamb()
    component.initialize()


def test_initialize():
    component = BmiIlamb()
    component.initialize(bmi_ilamb_config)


def test_initialize_n_arguments():
    component = BmiIlamb()
    component.initialize(bmi_ilamb_config)
    assert_equal(len(component.args), 5)


def test_initialize_sets_env_vars():
    component = BmiIlamb()
    component.initialize(bmi_ilamb_config)
    assert_true(os.environ.has_key('ILAMB_ROOT'))
    assert_true(os.environ.has_key('MPLBACKEND'))


def test_finalize():
    component = BmiIlamb()
    component.finalize()


def test_update():
    component = BmiIlamb()
    component.initialize(bmi_ilamb_config)
    if ilamb_is_installed():
        component.update()
    component.finalize()


def test_update_until():
    component = BmiIlamb()
    component.initialize(bmi_ilamb_config)
    if ilamb_is_installed():
        component.update_until(10.0)
    component.finalize()


def test_str():
    component = BmiIlamb()
    component.initialize(bmi_ilamb_config)
    s = str(component)
    assert_is(type(s), str)
