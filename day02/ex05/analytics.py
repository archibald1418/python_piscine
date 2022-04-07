from random import randint
from config import NUM_OF_STEPS, HAS_HEADER

class Research:

    data = []

    def __init__ (self, path):
        self.path = path

    class Calculations:
        def counts(data):
            heads_count = tails_count = 0
            
            for outcome in data:
                heads_count += outcome[0]
                tails_count += outcome[1]
            
            return heads_count, tails_count

        def fractions(heads_count, tails_count):
            total = heads_count + tails_count
            return heads_count / total, tails_count / total
    
    class Analytics(Calculations):
        
        
        @staticmethod
        def get_random_outcome():
            event = randint(0, 1)
            return [event, 1 - event]
            
        #NOTE: this is interesting
        # I can't access static method without mentioning the class name
        def predict_random(num_of_steps=NUM_OF_STEPS):
            return [Research.Analytics.get_random_outcome() for i in range(num_of_steps)]
        
        def predict_last():
            if not Research.data:
                return print("Data is empty")
            return Research.data[-1]
        
        def save_file(data, name_of_file, ext='txt'):
            pass
        

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