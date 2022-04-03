#!/bin/sh

BASE_URL='https://api.hh.ru'
USER_AGENT="'User-Agent: curl/7.71.1'"
JQ_FILTER="{page, found, clusters, arguments, per_page, pages, items}"
OUTFILE='hh.json'

echo "Enter vacancy name:\n"
read vacancy_name
echo "Vacanies per page?:\n"
read per_page
if [ -z $per_page ]; then
    per_page=20
fi;

echo $USER_AGENT

vacancy_name=$(echo $vacancy_name | xargs | tr ' ' '-')

curl -H $USER_AGENT $BASE_URL'/vacancies?describe_arguments=true&text='$vacancy_name'&per_page='$per_page'&page=0' | jq "$JQ_FILTER" > $OUTFILE;

