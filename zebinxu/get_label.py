from __future__ import print_function
from pyspark import SparkContext
import csv
from label import *

def save_label(rdd, col_index, label_file_pattern, basic_type, semantic_type, label_func):
    """ Map every row in a column to a tuple (basic_type, semantic_type, label) and save to file """
    rdd.map(lambda row: row[col_index - 7].strip()) \
        .map(lambda row: '%s\t%s\t%s\t%s' % (row, basic_type, semantic_type, label_func(row))) \
        .coalesce(1) \
        .saveAsTextFile(label_file_pattern.format(col_index))


sc = SparkContext()
filepath = './NYPD_Complaint_Data_Historic.csv'
data = sc.textFile(filepath)

# Header
header = data.first()

# Extract column 7 - 13
rdd = data.filter(lambda row: row != header) \
    .mapPartitions(lambda row: csv.reader(row)) \
    .map(lambda row: (row[6], row[7], row[8], row[9], row[10], row[11], row[12])).cache()


label_file_pattern = 'col{}_label.out' # Save for each row a tuple (basic type, semantic type, label) for every column. This tells if the value is VALID/INVALID/NULL

## Assign each value a tuple (basic_type, semantic_type, label), where label can be VALID/INVALID/NULL

# Column 7
save_label(rdd, 7, label_file_pattern, 'INT', 'THREE_DIGIT_CODE', check_three_digit)
# Column 8
save_label(rdd, 8, label_file_pattern, 'TEXT', 'DESCRIPTION', checknull)
# Column 9
save_label(rdd, 9, label_file_pattern, 'INT', 'THREE_DIGIT_CODE', check_three_digit)
# Column 10
save_label(rdd, 10, label_file_pattern, 'TEXT', 'DESCRIPTION', checknull)
# Column 11
save_label(rdd, 11, label_file_pattern, 'TEXT', 'INDICATOR', check_indicator)
# Column 12
save_label(rdd, 12, label_file_pattern, 'TEXT', 'OFFENSE_LEVEL', check_offense_level)
# Column 13
save_label(rdd, 13, label_file_pattern, 'TEXT', 'JURISDICTION', checknull)
