#!/bin/bash

module load python/gnu/3.4.4
export PYSPARK_PYTHON=/share/apps/python/3.4.4/bin/python
export PYTHONHASHSEED=0
export SPARK_YARN_USER_ENV=PYTHONHASHSEED=0
alias hfs='/usr/bin/hadoop fs'

function clean() {
    echo "cleaning local files..."
    if [ -d result ]; then
        rm -rf result
    fi
    echo "cleaning hdfs files..."
    if $(hfs -test -d result); then
	hfs -rm -r result
    fi
}

# Pull resutls from HDFS
function get() {
    echo "pull results from HDFS..."
    for x in 7 8 9 10 11 12 13; do
        hfs -getmerge "result/values_count/col${x}.out" "result/values_count/col${x}.csv"
        hfs -getmerge "result/label/col${x}.out" "result/label/col${x}.csv"
        hfs -getmerge "result/label_count/col${x}.out" "result/label_count/col${x}.csv"
    done
}

clean
spark2-submit get_values_count.py
spark2-submit get_label.py
spark2-submit get_label_count.py
get

