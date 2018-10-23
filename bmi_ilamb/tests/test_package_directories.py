"""Tests directories set in the package definition file."""

import os

from .. import package_dir, data_dir


def test_package_dir_is_set():
    assert package_dir is not None


def test_data_dir_is_set():
    assert data_dir is not None


def test_package_dir_exists():
    assert os.path.isdir(package_dir) is True


def test_data_dir_exists():
    assert os.path.isdir(data_dir) is True
