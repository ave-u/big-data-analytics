from __future__ import print_function
from pyspark import SparkContext
import csv
from label import *

def save_values_count(rdd, column_index, offset, file_pattern):
    """
        Aggregate the column based on column_index and count
        Each row is mapped to a tuple (value, count),
        where value is the original value (the only modification is that I strip the string) in the table,
        count is the times the value appears in the dataset.
        The result is finally saved as tab-separated key-value pairs with an ascending order in values.
    """
    count = rdd.map(lambda row: (row[column_index - offset].strip(), 1)) \
    .reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda row: row[1]) \
    .map(lambda row: '%s,%d' % (row[0], row[1])) \
    .coalesce(1) \
    .saveAsTextFile(file_pattern.format(column_index))


sc = SparkContext()
sc.addPyFile('label.py')
data = sc.textFile('./NYPD_Complaint_Data_Historic.csv')

# Header
header = data.first()

# Extract column 7 - 13
rdd = data.filter(lambda row: row != header) \
    .mapPartitions(lambda row: csv.reader(row)) \
    .map(lambda row: (row[6], row[7], row[8], row[9], row[10], row[11], row[12])).cache()


start_index = 7 # Starting index of the column
file_pattern = 'result/values_count/col{}.out'

# Initial inspection by aggregating each column separately and count and save
for i in range(start_index, 14):
    save_values_count(rdd, i, start_index, file_pattern)

sc.stop()
