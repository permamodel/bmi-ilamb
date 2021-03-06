[![Build Status](https://travis-ci.org/permamodel/bmi-ilamb.svg?branch=master)](https://travis-ci.org/permamodel/bmi-ilamb)
[![Code Health](https://landscape.io/github/permamodel/bmi-ilamb/master/landscape.svg?style=flat)](https://landscape.io/github/permamodel/bmi-ilamb/master)
[![Coverage Status](https://coveralls.io/repos/permamodel/bmi-ilamb/badge.svg?branch=master)](https://coveralls.io/r/permamodel/bmi-ilamb?branch=master)

# bmi-ilamb

A Basic Model Interface (BMI)
for version 2 (Python)
of the International Land Model Benchmarking Project (ILAMB)
benchmarking toolkit.

* The [journal article](http://dx.doi.org/10.1016/j.cageo.2012.04.002)
  that describes BMI
* ILAMB [home page](https://www.ilamb.org/)
* ILAMB [source code repository](https://bitbucket.org/ncollier/ilamb)
* ILAMB [documentation](https://ilamb.ornl.gov/doc/)

## Installation

Clone and install **bmi-ilamb** into a Python distribution with

    $ git clone https://github.com/permamodel/bmi-ilamb
    $ cd bmi-ilamb
    $ python setup.py install

ILAMB itself must also be installed;
follow the [instructions](https://ilamb.ornl.gov/doc/install.html)
in the ILAMB documentation
for downloading and installing ILAMB
into the same Python distribution as **bmi-ilamb**.

## Use

Two configuration files are needed:
one for ILAMB, the other for the BMI.
A description of the ILAMB configuration file can be found
in the ILAMB documentation.
The BMI configuration file contains values
that are passed to ILAMB's `ilamb-run` script.
Examples (
[ilamb.cfg](https://github.com/permamodel/bmi-ilamb/blob/master/bmi_ilamb/data/ilamb.cfg)
and
[bmi_ilamb.yaml](https://github.com/permamodel/bmi-ilamb/blob/master/bmi_ilamb/data/bmi_ilamb.yaml),
respectively)
are given in the **data** directory
of this repository.

In a Python session, execute:

```python
from bmi_lamb import BmiIlamb

m = BmiIlamb()
m.initialize('/path/to/bmi_ilamb.yaml')
m.update()  # calls the ilamb-run script
m.finalize()
```

The path to the BMI configuration file can be relative or absolute.

The result:
```bash
$ ls -F
_build/ log
```

View the run log with:

    $ cat log

Display ILAMB's graphical output with a web browser:

    $ firefox _build/index.html
