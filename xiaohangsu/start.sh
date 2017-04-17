rm "out/col*.out log/col*.log"

/usr/bin/hadoop fs -rm -r col*.out

for col in $@
do
    spark2-submit "col$col.py" | tee "log/col$col.log"
    /usr/bin/hadoop fs -getmerge "col$col.out" "out/col$col.out"
done


