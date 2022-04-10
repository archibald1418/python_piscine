#!/usr/bin/env python3


import os, sys
import requests
import bs4
from pprint import pprint
import pickle

# URL = 'https://finance.yahoo.com/quote/msft/financials?p=msft&guccounter=1'
URL = 'https://finance.yahoo.com/quote/{0}/financials?p={0}' # TODO: account for tickr
HEADERS = {'User-Agent': 'curl/7.64.1'}


def normalize_tickr(tickr):
    return tickr.lower()

def field_name_ok(field_name, expected_field_name):
    return hash(field_name.lower()) == hash(expected_field_name.lower())

def check_fields(field, field_names):
    for field_name in field_names:
        if field_name_ok(field, field_name):
            return field_name
    return None
    


if __name__ == '__main__':


    argc = len(sys.argv)
    if argc != 3:
        print("Bad args")
        exit()
    
    tickr, field = sys.argv[1:]
    
    
    resp = requests.get(url=URL.format(tickr), headers=HEADERS)
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
    
    real_field_name = check_fields(field, all_rows.keys())
    if real_field_name is None:
        raise Exception("Field not found")
    
    rowValue = tuple([real_field_name] + all_rows[real_field_name])
    print(rowValue)
    
