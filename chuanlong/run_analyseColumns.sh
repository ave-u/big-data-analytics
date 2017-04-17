rm summary.txt
/usr/bin/hadoop fs -rm -r L*.out
/usr/bin/hadoop fs -rm -r H*.out
/usr/bin/hadoop fs -rm -r *_*.out
spark-submit analyseColumns.py
