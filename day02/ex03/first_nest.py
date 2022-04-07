#!/usr/bin/env python3

import sys

class Research:

    def __init__ (self, path):
        self.path = path

    class Calculations:
        def counts(data):
            heads_count = tails_count = 0
            
            for outcome in data:
                heads_count += outcome[0]
                tails_count += outcome[1]
            
            return heads_count, tails_count

        def fractions(heads_count, tails_count):
            total = heads_count + tails_count
            return heads_count / total, tails_count / total

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

    @staticmethod
    def validate_header(header):
        split = header.split(',')
        if len(split) != 2 or not all(split):
            raise Exception("Bad header")
        
    def file_reader(self, has_header=True):
        arr = []
        with open(self.path, 'r') as csvfile:
            if has_header:
                header = csvfile.readline().strip()
                Research.validate_header(header)
            for line in csvfile:
                row = line.strip().split(',')
                Research.validate_row(row)
                row[0], row[1] = int(row[0]), int(row[1])
                arr.append(row)
        return arr

if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print("Bad args")
        exit()

    r = Research(sys.argv[1])

    try:
        # print(*r.file_reader(), sep='', end='')
        data = r.file_reader()
        print(data)
        heads_count, tails_count = r.Calculations.counts(data)
        print(heads_count, tails_count)
        heads_fractions, tails_fractions = r.Calculations.fractions(heads_count, tails_count)
        print(heads_fractions, tails_fractions)
    except Exception as e:
        print(e)