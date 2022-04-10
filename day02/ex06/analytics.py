from random import randint
from config import NUM_OF_STEPS, HAS_HEADER, \
        LOG_FILE, REPORT_FILE
import logging
import os
import json

logging.basicConfig(filename=LOG_FILE,
                    level='INFO',
                    format='%(asctime)s:%(message)s',
                    datefmt='%y-%d-%m %H:%M:%S',
                    filemode='w')

def decorator_factory(msg=None):
    def log_decorator(func):
        def wrapper(*args, **kwargs):
            logging.info(msg)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return log_decorator 



class Research:

    data = []

    def __init__ (self, path):
        self.path = path

    class Calculations:

        _MSG_COUNTS = 'Calculating the counts of heads and tails'
        _MSG_FRACTIONS = 'Calculating fractions of heads and tails'

        @decorator_factory(msg=_MSG_COUNTS)
        def counts(data):
            heads_count = tails_count = 0
            
            for outcome in data:
                heads_count += outcome[0]
                tails_count += outcome[1]
            
            return heads_count, tails_count

        @decorator_factory(msg=_MSG_FRACTIONS)
        def fractions(heads_count, tails_count):
            total = heads_count + tails_count
            return heads_count / total, tails_count / total
    
    class Analytics(Calculations):
        
        _MSG_PREDICT_RANDOM = f'Predicting %s random outcomes' % (NUM_OF_STEPS)
        _MSG_PREDICT_LAST = 'Predicting last outcome'
        _MSG_SAVE_FILE = f'Saving file to %s ' % (REPORT_FILE)

        @staticmethod
        def get_random_outcome():
            event = randint(0, 1)
            return [event, 1 - event]
            
        #NOTE: this is interesting
        # I can't access static method without mentioning the class name
        
        @decorator_factory(msg=_MSG_PREDICT_RANDOM)
        def predict_random(num_of_steps=NUM_OF_STEPS):
            return [Research.Analytics.get_random_outcome() for i in range(num_of_steps)]
        
        @decorator_factory(msg=_MSG_PREDICT_LAST)
        def predict_last():
            if not Research.data:
                return print("Data is empty")
            return Research.data[-1]
        
        @decorator_factory(msg=_MSG_SAVE_FILE)
        def save_file(report, name_of_file=REPORT_FILE, ext='txt'):
            with open(f'{REPORT_FILE}.{ext}', 'w') as report_file:
                report_file.write(report)
        

    @staticmethod
    def validate_row(row):
        if len(row) != 2:
            raise Exception("Bad row")
        try:
            i, j = row
            if (i not in ('0', '1')) or (j not in ('0', '1')):
                raise Exception("Row values must be 0 or 1")
            if i == j:
                raise Exception("Row values must be different")
        except ValueError:
            raise Exception("Bad row values: can't convert to int")

    @staticmethod
    def validate_header(header):
        split = header.split(',')
        if len(split) != 2 or not all(split):
            raise Exception("Bad header")
        
    def file_reader(self, has_header=HAS_HEADER):
        arr = []
        with open(self.path, 'r') as csvfile:
            if has_header:
                header = csvfile.readline().strip()
                Research.validate_header(header)
            for line in csvfile:
                row = line.strip().split(',')
                Research.validate_row(row)
                row[0], row[1] = int(row[0]), int(row[1])
                arr.append(row)
        Research.data = arr.copy()
        return arr
    
    @staticmethod
    def send_message(request):
        print(request)
        os.system(request)
