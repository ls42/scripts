#!/usr/bin/env python3

# Create hash of file and compare it with a string from the command line

from hashlib import sha256
import argparse
import os
import sys

parser = argparse.ArgumentParser('Verify sha256 hash of file')
parser.add_argument('-f', '--filename', type=str,
                    help='File that needs hashing', required=True)
parser.add_argument('-s', '--filesum', type=str,
                    help='Correct hashsum of that file', required=True)
parser.add_argument('-v', '--verbose',
                    help='Print actual and expected hashsums', action='store_true')
args = parser.parse_args()


class tcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    NORMAL = '\033[0m'


try:
    file_obj = open(args.filename, 'rb')
except FileNotFoundError as e:
    print(str(e))
    sys.exit()
real_sum = sha256(file_obj.read()).hexdigest()
if args.verbose:
    print('actual:   {}\nexpected: {}'.format(real_sum, args.filesum))
if real_sum == args.filesum:
    print('{}OK{}'.format(tcolors.OK, tcolors.NORMAL))
else:
    print('{}NOK{}'.format(tcolors.FAIL, tcolors.NORMAL))
