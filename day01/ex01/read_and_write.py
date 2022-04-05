#!/usr/bin/env python3 


INFILE='ds.csv'
OUTFILE='ds.tsv'

def is_quote(char):
    return char == '\'' or char == '\"'

def read_and_write(infile=INFILE, outfile=OUTFILE):
    
    import os
    print(os.listdir())

    with open(infile, 'r') as ifstream:
        with open(outfile, 'w') as ofstream:
            quote = ''
            for line in ifstream:
                for i in range(len(line)):
                    char = line[i]
                    if is_quote(line[i]):
                        if quote == line[i]:
                            quote = ''
                        else:
                            quote = line[i]
                    elif line[i] == ',' and not quote:
                        char = '\t'
                    ofstream.write(char)
                    print(char,end='')
            ofstream.write('\n')
            print()

if __name__ == '__main__':
    read_and_write()