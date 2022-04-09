#!/usr/bin/env python3 

import os

def print_env():
    print(f'Your current virtual env is %s' % (os.environ["VIRTUAL_ENV"]))

if __name__ == '__main__':
    print_env()
