#!/usr/bin/env python3


import os, sys
from xml.dom.minidom import Element
import requests
import bs4
from pprint import pprint
import pickle

# URL = 'https://finance.yahoo.com/quote/msft/financials?p=msft&guccounter=1'
URL = 'https://finance.yahoo.com/quote/msft/financials' # TODO: account for tickr
HEADERS = {'User-Agent': 'curl/7.64.1'}


if __name__ == '__main__':


    argc = len(sys.argv)
    if argc != 3:
        print("Bad args")
        exit()
    
    tickr, field = sys.argv[1:]
    
    resp = requests.get(url=URL, headers=HEADERS)
    if resp.status_code == 404:
        raise Exception("URL not found")
    
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    
    header: bs4.element.Tag = list(
        map(
            lambda x: x.contents[0],
            soup.find("div", {"class": "D(tbhg)"}).findAll('span')))
    all_rows: bs4.element.Tag  = list(
        map(
            lambda x: list(
                map(
                    lambda y: y.contents[0], 
                    x.findAll('span'))),
            soup.findAll("div", {"data-test":"fin-row"})))
    
    all_rows = dict({row[0]: list(row[1:]) for row in all_rows})
    
    if field not in all_rows:
        raise Exception("Field not found")
    
    rowValue = tuple([field] + all_rows[field])
    print(rowValue)
    
