#!/usr/bin/env python3

import os, sys
import requests
import urllib3
import bs4
from pprint import pprint
import time
import pickle
import cProfile

# URL = 'https://finance.yahoo.com/quote/msft/financials?p=msft&guccounter=1'
URL = 'https://finance.yahoo.com/quote/{0}/financials?p={0}' # TODO: account for tickr
HEADERS = {'User-Agent': 'curl/7.64.1'}


def normalize_tickr(tickr):
    return tickr.lower()

def field_name_ok(field_name, expected_field_name):
    return hash(field_name.lower()) == hash(expected_field_name.lower())

def field_name_basic(field_name, expected_field_name):
    return hash(field_name) == hash(expected_field_name)

def check_fields(field, field_names, field_checker=field_name_ok):
    for field_name in field_names:
        if field_checker(field, field_name):
            return field_name
    return None

def get_table_from_html(response_text):
    soup = bs4.BeautifulSoup(response_text, 'html.parser')
    
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
    
    table = dict({row[0]: row[1:] for row in all_rows})
    return header, table 

def main(argv=sys.argv):
    argc = len(argv)
    if argc != 3:
        print("Bad args")
        exit()
    
    tickr, field = argv[1:]
    try:
        resp = requests.get(url=URL.format(tickr), headers=HEADERS)
        if resp.status_code == 404:
            raise Exception("URL not found")
    except requests.exceptions.ConnectionError as e:
        print("URL NOT FOUND")

    # time.sleep(5)
    
    header, all_rows = get_table_from_html(resp.text)
    real_field_name = check_fields(field, all_rows.keys())
    if real_field_name is None:
        raise Exception("Field not found")
    
    rowValue = tuple([real_field_name] + all_rows[real_field_name])
    print(rowValue)


FILENAME = os.path.basename(__file__)
TEST1 = [FILENAME, "MSFT", "Total Revenue"]

if __name__ == '__main__':
    import cProfile, pstats

    profiler = cProfile.Profile()
    
    profiler.enable()
    # Code to profile goes here

    main(TEST1)

    profiler.disable()

    # Analyze stats
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats(5)
    
