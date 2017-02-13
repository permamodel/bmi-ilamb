"""Unit tests for the bmi-ilamb package."""

import subprocess


def ilamb_is_installed():
    try:
        subprocess.call(['ilamb-run', '--help'])
    except OSError:
        return False
    else:
        return True
