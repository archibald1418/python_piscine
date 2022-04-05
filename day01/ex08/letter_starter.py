#!/usr/bin/env python3

import sys

TEMPLATE = f'''Dear %s, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.

We are delighted to greet you in our team!

Always yours,
Horns & Hooves.CO

!!!
'''

def start_letter(infile, name, delim='\t'):
    
    with open(infile, 'r') as names:
        header = names.readline()
        columns = names.readline()
        for line in names:
            row = line.split(delim)
            if name == row[1].strip():
                fmt = TEMPLATE % (name,)
                return fmt[:fmt.find('\n')]

    return f"{name} not found!"
            
        

if __name__ == '__main__':
    
    argc = len(sys.argv)
    if argc != 3:
        print("Wrong args")
        exit()
    
    infile = sys.argv[1]
    name = sys.argv[2]
    print(start_letter(infile, name.lower().capitalize()))