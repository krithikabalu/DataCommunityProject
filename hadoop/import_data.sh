#!/usr/bin/env bash
sqoop import --connect jdbc:postgresql://postgres:5432/postgres?user=postgres --table $1

echo "Listing hdfs contents"

/usr/local/hadoop/bin/hdfs dfs -ls $1