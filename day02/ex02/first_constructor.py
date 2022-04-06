#!/usr/bin/env python3

import sys

class Research:

    def __init__ (self, path):
        self.path = path
    
    @staticmethod
    def validate_row(row):
        if len(row) != 2:
            raise Exception("Bad row")
        try:
            i, j = row
            if (i not in ('0', '1')) or (j not in ('0', '1')):
                raise Exception("Row values must be 0 or 1")
            if i == j:
                raise Exception("Row values must be different")
        except ValueError:
            raise Exception("Bad row values: can't convert to int")

    def file_reader(self):
        with open(self.path, 'r') as csvfile:
            header = csvfile.readline().strip()
            split = header.split(',')
            if len(split) != 2 or not all(split):
                raise Exception("Bad header")
            yield header + '\n'
            for line in csvfile:
                row = line.strip().split(',')
                Research.validate_row(row)
                yield line

if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print("Bad args")
        exit()

    r = Research(sys.argv[1])

    try:
        print(*r.file_reader(), sep='', end='')
    except Exception as e:
        print(e)