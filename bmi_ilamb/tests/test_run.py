import os
import subprocess
from nose.tools import raises, assert_equal
from .. import ILAMB_ROOT
from bmi_ilamb.cmd.run import parse_arguments, main


cmd = 'ilamb2-run'


def setup_module():
    """Fixture called before any tests are performed."""
    print('\n*** ' + __name__)
    try:
        os.environ['ILAMB_ROOT']
    except KeyError:
        os.environ['ILAMB_ROOT'] = ILAMB_ROOT


def test_help_argument():
    r = subprocess.call([cmd, '--help'])
    assert_equal(r, 0)


@raises(subprocess.CalledProcessError)
def test_fails_without_config_file():
    r = subprocess.check_call([cmd])
