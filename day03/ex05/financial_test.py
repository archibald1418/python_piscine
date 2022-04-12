import os, sys
import pytest
import re

# Set up script
app_path = os.path.abspath(os.pardir)
print(app_path)
sys.path.append(app_path)

# import the tested and the errors
from ex03.financial import main, TickerNotFound


# Test cases
ARGS_OK = ["", 'msft', 'Total Revenue']
ARGS_BAD_TICKER = ["", 'asldfjhals', "Total Revenue"]

# Test functions
def test_total_revenue():
    assert main(ARGS_OK)[0].lower() == 'Total Revenue'.lower()

def test_is_tuple():
    assert isinstance(main(ARGS_OK), tuple)


def test_invalid_ticker_error():
    # connection error check failed; url comparison ok
    with pytest.raises(TickerNotFound, match='TICKER NOT FOUND', ):
        main(ARGS_BAD_TICKER)
    

"""
•   If I ask for Total Revenue, do I get the total revenue for the given ticker?
•   Is the type of the return a tuple?
•   If I give an invalid ticker name, do I get an exception?
"""
    
    