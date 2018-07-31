#!/usr/bin/env python3

# Create hash of file and compare it with a string from the command line

from hashlib import sha256
import argparse
import os

parser = argparse.ArgumentParser('Verify sha256 hash of file')
parser.add_argument('-f', '--filename', type=str,
                    help='File that needs hashing', required=True)
parser.add_argument('-s', '--filesum', type=str,
                    help='Correct hashsum of that file', required=True)
args = parser.parse_args()


class tcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    NORMAL = '\033[0m'


file_obj = open(args.filename, 'rb')
real_sum = sha256(file_obj.read()).hexdigest()
if real_sum == args.filesum:
    print('{}OK.{}'.format(tcolors.OK, tcolors.NORMAL))
else:
    print('{}NOK{}'.format(tcolors.FAIL, tcolors.NORMAL))
