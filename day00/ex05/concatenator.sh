INFILE=../ex03/hh_positions.csv

dates=$(awk -F"[T,]" '{print $2}' $INFILE | tr -d '"')

echo $dates;