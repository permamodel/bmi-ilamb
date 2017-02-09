import os
from .bmi_ilamb import BmiIlamb
from .config import Configuration


__all__ = ['BmiIlamb', 'Configuration']
__version__ = 0.1

package_dir = os.path.dirname(__file__)
data_dir = os.path.join(package_dir, 'data')
