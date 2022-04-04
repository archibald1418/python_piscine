#!/bin/sh

export BASE_URL='https://api.hh.ru'
export GET_VACANCIES=$BASE_URL'/vacancies'
export USER_AGENT="'User-Agent: curl/7.71.1'"
export COLS='["id","created_at","name","has_test","alternate_url"]'
export VALS='[.id,.created_at,.name,.has_test,.alternate_url]'



echo "Enter vacancy name:\n"
read vacancy_name
per_page=10

vacancy_name=$(echo $vacancy_name | xargs | tr ' ' '-')

# echo "Vacanies per page?:\n"
# read per_page
# if [ -z $per_page ]; then
#     per_page=20
# fi;

echo $COLS;
echo $VALS;

curl -H $USER_AGENT $BASE_URL'/vacancies?text='$vacancy_name | jq -r -f filter.jq > hh.csv;