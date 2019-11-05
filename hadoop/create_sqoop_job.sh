#!/usr/bin/env bash
sqoop job --create myjob -- import --connect jdbc:postgresql://postgres:5432/postgres?user=postgres --table $1 --incremental append --check-column $2 --last-value $3

#sqoop job --exec myjob

echo "Listing jobs"

sqoop job --list
