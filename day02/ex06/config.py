import re

NUM_OF_STEPS = 3
HAS_HEADER = True
REPORT_TEMPLATE = f"""
We have made %d observations from tossing a coin:
%d of them were tails and
%d of them were heads.
The probabilities are %.2f%% and %.2f%%, respectively.

Our forecast is that in the next %d observations we will have:
%d tails and %d heads."""

LOG_FILE = "analytics.log"
REPORT_FILE = 'report'

LOG_STATUS_OK_JSON = {"text": "The report has been successfully created"}
LOG_STATUS_FAIL_JSON = {"text": "The report hasn\\u0027t been created due to an error"}

SLACK_WEBHOOK = 'https://hooks.slack.com/services/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'
LOG_REQUEST_FAIL = f"curl -X POST -H 'Content-type: application/json' --data \"{LOG_STATUS_FAIL_JSON}\" {SLACK_WEBHOOK}"
LOG_REQUEST_OK = f"curl -X POST -H 'Content-type: application/json' --data '{LOG_STATUS_OK_JSON}' {SLACK_WEBHOOK}"