#!/bin/sh

INFILE=../ex03/hh_positions.csv
OUTFILE=hh_uniq_positions.csv

printf '"%s","%s"\n' 'name' 'count' > $OUTFILE;
tail -n +2 $INFILE | awk -F"," '{col[$3]++} END {for (i in col) printf "%s,%s\n",i,col[i]}' >> $OUTFILE