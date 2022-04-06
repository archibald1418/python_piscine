#!/usr/bin/env python3

import sys

ALPHABET = ''.join([chr(c) for c in range(ord('a'), ord('z') + 1)])
LENGTH = ord('z') - ord('a')
START = ord('a')
END = ord('z')

def shift_letter(c, shift): 
    if not c.isalpha():
        return c
    return chr((ord(c) - ord('a') + shift) % (LENGTH + 1) + ord('a'))

def encode(s, shift):
    for c in s:
        yield shift_letter(c, shift)

def decode(s, shift):
    for c in s:
        yield shift_letter(c, -shift)
    

def main():
    argc = len(sys.argv)
    if argc != 4:
        print("Wrong arguments")
        exit()
    if sys.argv[1] == 'decode':
        return print(''.join(decode(s = sys.argv[2], shift = int(sys.argv[3]))))
    if sys.argv[1] == 'encode':
        return print(''.join(encode(s = sys.argv[2], shift = int(sys.argv[3]))))


if __name__ == '__main__':
    main()
    
    # s = 'ssh -i private.key user@school21.ru'
     