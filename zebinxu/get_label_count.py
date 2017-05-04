from __future__ import print_function
from pyspark import SparkContext
import csv
from label import *

def save_label_count(rdd, col_index, count_file_pattern, basic_type, semantic_type, label_func):
    """ Group by label column and count and save """ 
    rdd.map(lambda row: (label_func(row[col_index - 7].strip()), 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .map(lambda row: '%s,%s,%s,%d' % (basic_type, semantic_type, row[0], row[1])) \
        .coalesce(1) \
        .saveAsTextFile(count_file_pattern.format(col_index))


sc = SparkContext()
sc.addPyFile('label.py')
data = sc.textFile('./NYPD_Complaint_Data_Historic.csv')

# Header
header = data.first()

# Extract column 7 - 13
rdd = data.filter(lambda row: row != header) \
    .mapPartitions(lambda row: csv.reader(row)) \
    .map(lambda row: (row[6], row[7], row[8], row[9], row[10], row[11], row[12])).cache()


count_file_pattern = 'result/label_count/col{}.out' # Save for each row a tuple (basic type, semantic type, label, count) for each column 

## Aggregate and count the label for each column. 
#Each row is assigned the count (last column) for the label (second last column): (basic_type, semantic_type, label, count)

# Column 7
save_label_count(rdd, 7, count_file_pattern, 'INT', 'THREE_DIGIT_CODE', check_three_digit)
# Column 8
save_label_count(rdd, 8, count_file_pattern, 'TEXT', 'DESCRIPTION', checknull)
# Column 9
save_label_count(rdd, 9, count_file_pattern, 'INT', 'THREE_DIGIT_CODE', check_three_digit)
# Column 10
save_label_count(rdd, 10, count_file_pattern, 'TEXT', 'DESCRIPTION', checknull)
# Column 11
save_label_count(rdd, 11, count_file_pattern, 'TEXT', 'INDICATOR', check_indicator)
# Column 12
save_label_count(rdd, 12, count_file_pattern, 'TEXT', 'OFFENSE_LEVEL', check_offense_level)
# Column 13
save_label_count(rdd, 13, count_file_pattern, 'TEXT', 'JURISDICTION', checknull)


sc.stop()    
