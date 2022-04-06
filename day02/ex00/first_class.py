#!/usr/bin/env python3

class Must_read:
    
    with open('./data.csv', 'r') as csvfile:
        print(csvfile.read(), end='')

if __name__ == '__main__':
    
    Must_read()