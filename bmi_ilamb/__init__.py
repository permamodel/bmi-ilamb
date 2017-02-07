import os
from .bmi_ilamb import BmiIlamb


__all__ = ['BmiIlamb']
__version__ = 0.1

package_dir = os.path.dirname(__file__)
data_dir = os.path.join(package_dir, 'data')
