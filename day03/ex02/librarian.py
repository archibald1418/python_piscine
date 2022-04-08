#!/usr/bin/env python3

import os

ENVIRON = 'ldonita'
REQUIREMENTS = 'requirements.txt'

def install_req():
    
    if os.environ.get("VIRTUAL_ENV") is None:
        raise Exception("Activate your environment")

    if os.environ.get("VIRTUAL_ENV")[os.environ.get("VIRTUAL_ENV").rfind('/') + 1:] != ENVIRON:
        raise Exception(f"Environment is not {ENVIRON}")

    os.system(f"pip install -r {REQUIREMENTS}")
    os.system(f"pip freeze > {REQUIREMENTS}")

if __name__ == '__main__':
    install_req()
