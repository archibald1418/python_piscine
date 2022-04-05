#!/usr/bin/env python3

import sys

COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
}

STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
}


def stock_prices(names: list, count):
    for i in range(count - 1):
        print(STOCKS.get(COMPANIES.get(names[i].capitalize(), None), "Unknown company"))

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 2:
        print("Not enough arguments")
        exit()
    stock_prices(sys.argv[1:], argc)