NUM_OF_STEPS = 3
HAS_HEADER = True
REPORT_TEMPLATE = f"""Report
We have made %d observations from tossing a coin:
%d of them were tails and
%d of them were heads.
The probabilities are %.2f%% and %.2f%%, respectively.

Our forecast is that in the next %d observations we will have:
%d tails and %d heads."""

REPORT_FILE = 'report'