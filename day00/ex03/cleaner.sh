#!/bin/sh

INFILE=../ex02/hh_sorted.csv
OUTFILE=hh_positions.csv

# Copy header
head -n 1 $INFILE > $OUTFILE;
# awk '{$35 = $35"$"; print}' infile > outfile


# Start scanning
tail -n +2 $INFILE | {
while IFS= read -r line
    do
        match=$(echo $line | grep -Eio '(senior|junior|middle)')
        joined=$(echo $match | xargs | sed -E 's/ /\//g')
        if [ -z $joined ]; then
            joined='-'
        fi
        echo "$line" | awk -F"," -v val=\"$joined\" '{OFS=","}{$3=val; print $0}' >> $OUTFILE
    done
}