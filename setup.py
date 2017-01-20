from setuptools import setup, find_packages
from bmi_ilamb import __version__


setup(name='bmi-ilamb',
      version=__version__,
      description='BMI for ILAMB',
      long_description=open('README.md').read(),
      url='https://github.com/permamodel/bmi-ilamb',
      license='MIT',
      author='Mark Piper',
      author_email='mark.piper@colorado.edu',
      packages=find_packages(exclude=['*.tests']),
      entry_points={
          'console_scripts': [
              'ilamb2-run=bmi_ilamb.cmd.run:main',
          ],
      },
      keywords='CSDMS BMI ILAMB model benchmark',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
      ],
)