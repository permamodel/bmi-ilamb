"""Run an ILAMB experiment."""

import os
import sys
import subprocess
import argparse
from .. import ILAMB_ROOT


def parse_arguments(args):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('config_file', help='ILAMB configuration file')
    parser.add_argument('--models-dir',
                        default=os.path.join(os.environ['ILAMB_ROOT'], 'MODELS'),
                        help='path to model output')
    parser.add_argument('--output-dir',
                        default='ILAMB-output',
                        help='output directory')
    parser.add_argument('--regions',
                        default='global',
                        help='locale of calculations')
    parser.add_argument('--wmt-executor',
                        default='/home/csdms/wmt/_testing',
                        help='path to WMT executor')
    return parser.parse_args(args)


def main():
    try:
        os.environ['ILAMB_ROOT']
    except KeyError:
        os.environ['ILAMB_ROOT'] = ILAMB_ROOT

    os.environ['MPLBACKEND'] = 'Agg'

    args = parse_arguments(sys.argv[1:])

    driver = os.path.join(args.wmt_executor, 'opt', 'ilamb', 'demo', 'driver.py')

    cmd = ['python', driver,
           '--config=%s' % args.config_file,
           '--model_root=%s' % args.models_dir,
           '--build_dir=%s' % args.output_dir,
           '--regions=%s' % args.regions
    ]

    with open('ilamb.stdout', 'w') as stdout:
        with open('ilamb.stderr', 'w') as stderr:
            subprocess.check_call(cmd, stdout=stdout, stderr=stderr)

    
if __name__ == '__main__':
    main()
