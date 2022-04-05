#!/bin/sh

INFILE=../ex03/hh_positions.csv

awk -F"[T,]" '{print $2}' $INFILE | tr -d '"' | xargs rm -rf

tail -n +2 $INFILE | while IFS="" read line 
    do 
        date=$(echo $line | awk -F"[T,]" '{print $2}' | tr -d '"')
        echo $date;
        if [ ! -f "$date" ]; then
            echo 'kek';
            head -n 1 $INFILE > $date;
        fi;
        echo $line >> "$date";
    done