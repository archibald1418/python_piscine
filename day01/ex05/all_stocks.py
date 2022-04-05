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



def parse_stock(args: list, count):
    for i in range(count ):
        found_company = found_ticker = False
        for company, ticker in COMPANIES.items():
            if args[i].upper() == COMPANIES[company]:
                found_ticker = True
                print(f'%s is a ticker symbol for %s' % (ticker.upper(), company))
                break;
            elif args[i].capitalize() == company:
                found_company = True
                print(f'%s stock price is %s' % (company, STOCKS[COMPANIES[company]]))
                break;
        if not (found_ticker or found_company):
            print(f"{args[i]} is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc != 2:
        print("Wrong args. I need one string")
        exit()
    args = list(map(str.strip, sys.argv[1].split(',')))
    if not all(args):
        exit()

    parse_stock(args, len(args))