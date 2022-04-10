#!/usr/bin/env python3

from analytics import Research
from config import REPORT_TEMPLATE, NUM_OF_STEPS, REPORT_FILE, LOG_STATUS_FAIL_JSON, LOG_STATUS_OK_JSON
import os

from config import LOG_REQUEST_FAIL, LOG_REQUEST_OK


if __name__ == '__main__':
    
    if len(os.sys.argv) != 2:
        print("Bad args")
        exit()

    r = Research(os.sys.argv[1])

    try:
        # print(*r.file_reader(), sep='', end='')
        data = r.file_reader()
        heads_count, \
            tails_count = r.Calculations.counts(data)
        observations = heads_count + tails_count
        heads_fractions, \
            tails_fractions = r.Calculations.fractions(heads_count, tails_count)
        prediction = Research.Analytics.predict_random(NUM_OF_STEPS)
        predict_last = Research.Analytics.predict_last()
        predict_heads_count, \
            predict_tails_count = Research.Calculations.counts(prediction)

        report = REPORT_TEMPLATE % (
        observations, 
        heads_count, 
        tails_count,
        heads_fractions * 100,
        tails_fractions * 100,
        NUM_OF_STEPS,
        predict_heads_count,
        predict_tails_count
        )
        r.Analytics.save_file(report)

        raise Exception("Test")
        
    except Exception as e:
        print(e)
        Research.send_message(LOG_REQUEST_FAIL)
    else:
        Research.send_message(LOG_REQUEST_OK)
    print("\nReport ok")