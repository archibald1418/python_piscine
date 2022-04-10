#!/usr/bin/env python3


import os, sys
import requests
import bs4
from pprint import pprint

# URL = 'https://finance.yahoo.com/quote/msft/financials?p=msft&guccounter=1'
URL = 'https://finance.yahoo.com/quote/msft/financials'
HEADERS = {'User-Agent': 'curl/7.64.1'}



if __name__ == '__main__':


    argc = len(sys.argv)
    if argc != 3:
        print("Bad args")
        exit()
    # try:
    resp = requests.get(url=URL, headers=HEADERS)
    if resp.status_code == 404:
        raise Exception("URL not found")
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    print(soup.prettify())