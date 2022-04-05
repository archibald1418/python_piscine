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


def ticker_symbols(tickers: list, count):
    for i in range(count - 1):
        found = False
        for company, ticker in COMPANIES.items():
            if tickers[i].upper() == COMPANIES[company]:
                found = True
                print(company, STOCKS[ticker], sep=' ')
        if not found:
            print("Unknown ticker")

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 2:
        print("Not enough arguments")
        exit()
    ticker_symbols(sys.argv[1:], argc)