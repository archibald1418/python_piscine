#!/usr/bin/env python3

import sys

PATTERN = 'name.surname@corp.com'

OUTFILE = 'employees.tsv'

def make_table(infile, delim='\t'):
    
    header = ["A", "B", "C"]
    columns = ["Name", "Surname", "E-mail"]
    with open(infile, 'r') as emails:
        with open(OUTFILE, 'w') as outfile:
            outfile.write(delim + delim.join(header) + '\n')
            outfile.write(delim + delim.join(columns) + '\n')
            i = 1
            for email in emails:
                email = email.strip()
                dot = email.find('.')
                at = email.find('@')
                if dot != -1 and at != -1:
                    name = email[:dot].capitalize()
                    surname = email[dot + 1: at].capitalize()
                    outfile.write(f'{i}{delim}{name}{delim}{surname}{delim}{email}\n')
                    i += 1
                    
if __name__ == '__main__':
    
    argc = len(sys.argv)
    if argc != 2:
        print("Wrong args")
        exit()
    
    infile = sys.argv[1]
    make_table(infile)