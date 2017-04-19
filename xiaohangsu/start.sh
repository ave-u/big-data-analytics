module load python/gnu/3.4.4
export PYSPARK_PYTHON=/share/apps/python/3.4.4/bin/python
export PYTHONHASHSEED=0
export SPARK_YARN_USER_ENV=PYTHONHASHSEED=0

rm -r out/ log/ plotData/
/usr/bin/hadoop fs -rm -r col*.out

mkdir log
mkdir out
mkdir plotData

for col in $@
do
    spark2-submit "col$col.py" | tee "log/col$col.log"
    /usr/bin/hadoop fs -getmerge "col$col.out" "out/col$col.out"
    if (($col == 2))
    then
        /usr/bin/hadoop fs -getmerge "col${col}_year.out" "plotData/col${col}_year.out"
        /usr/bin/hadoop fs -getmerge "col${col}_month.out" "plotData/col${col}_month.out"
        /usr/bin/hadoop fs -getmerge "col${col}_day.out" "plotData/col${col}_day.out"

        /usr/bin/hadoop fs -getmerge "col${col}_date_group.out" "plotData/col${col}_date_group.out"
    fi
    if (($col == 3))
    then
        /usr/bin/hadoop fs -getmerge "col${col}_time_group.out" "plotData/col${col}_time_group.out"
        /usr/bin/hadoop fs -getmerge "col${col}_hour.out" "plotData/col${col}_hour.out"

    fi
    if (($col == 14))
    then
        /usr/bin/hadoop fs -getmerge "col${col}_borough.out" "plotData/col${col}_borough.out"
    fi
done

