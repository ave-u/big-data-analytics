from __future__ import print_function
from pyspark import SparkContext
import csv

"""
    A script that generates labels and their count for the data in column 7 - 13 in NYPD_Complaint_Data_Historic.csv.
    Column 7: KY_CD
    Column 8: OFENS_DESC
    Column 9: PD_CD
    Column 10: PD_DESC
    Column 11: CRM_ATPT_CPTD_CD
    Column 12: LAW_CAT_CD
    Column 13: JURIS_DESC
"""

def check_three_digit(str):
    """ 
        Check values in column 7 and 9 (three digit) and label them with NULL/INVALID/VALID 
        
        NULL: value contains empty string or 'NULL'
        INVALID: length of the value is not 3 or the value is not numeric
        VALID: a three digit number
    """

    str = str.strip()
    if str == '' or str == 'NULL':
        return 'NULL'
    elif len(str) != 3:
        return 'INVALID'
    else:
        return ('VALID' if str.isdigit() else 'INVALID')

def check_indicator(str):
    """ 
        Check values in column 11 (indicator) and label them with NULL/INVALID/VALID

        NULL: value contains empty string or 'NULL'
        INVALID: the string is not one of "COMPLETED" and "ATTEMPTED" (case insensitive)
        VALID: one of "COMPLETED" and "ATTEMPTED"
    """

    str = str.strip()
    if str == '' or str == 'NULL':
        return 'NULL'
    
    str = str.upper() # Convert to upper case
    if str == 'COMPLETED' or str == 'ATTEMPTED':
        return 'VALID'
    else:
        return 'INVALID'

def check_offense_level(str):
    """ 
        Check values in column 12 (offense level) and label them with NULL/INVALID/VALID

        NULL: value contains empty string or 'NULL'
        INVALID: the string is not one of "felony", "misdemeanor", and "violation" (case insensitive)
        VALID: one of "felony", "misdemeanor", and "violation"
    """

    str = str.strip()
    if str == '' or str == 'NULL':
        return 'NULL'
    
    str = str.upper() # Convert to upper case
    if str == 'FELONY' or str == 'MISDEMEANOR' or str == 'VIOLATION':
        return 'VALID'
    else:
        return 'INVALID'

def checknull(str):
    return ('VALID' if str != '' else 'NULL')

def aggregate_and_count(rdd, column_index, offset):
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
    .map(lambda row: '%s\t%d' % (row[0], row[1])) \
    .coalesce(1) \
    .saveAsTextFile('col{0}.txt'.format(column_index))

def save_label(rdd, col_index, label_file_pattern, basic_type, semantic_type, label_func):
    """ Map every row in a column to a tuple (basic_type, semantic_type, label) and save to file """
    rdd.map(lambda row: row[col_index - 7].strip()) \
        .map(lambda row: '%s\t%s\t%s' % (basic_type, semantic_type, label_func(row))) \
        .coalesce(1) \
        .saveAsTextFile(label_file_pattern.format(col_index))
    
def save_label_count(rdd, col_index, count_file_pattern, basic_type, semantic_type, label_func):
    """ Group by label column and count and save """ 
    rdd.map(lambda row: (label_func(row[col_index - 7].strip()), 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .map(lambda row: '%s\t%s\t%s\t%d' % (basic_type, semantic_type, row[0], row[1])) \
        .coalesce(1) \
        .saveAsTextFile(count_file_pattern.format(col_index))


sc = SparkContext()
filepath = './NYPD_Complaint_Data_Historic.csv'
data = sc.textFile(filepath)

# Header
header = data.first()

# Extract column 7 - 13
rdd = data.filter(lambda row: row != header) \
    .mapPartitions(lambda row: csv.reader(row)) \
    .map(lambda row: (row[6], row[7], row[8], row[9], row[10], row[11], row[12])).cache()


# Initial inspection by aggregating each column separately and count and save
#for i in range(7, 14):
#    aggregate_and_count(rdd, i, INDEX_OFFSET)


# After inspecting the aggregated results, we now perform for the value in each column a mapping to a tuple (basic type, semantic type, label)
col_index = 7 # Starting index of the column
label_file_pattern = 'col{}_label.txt' # Save for each row a tuple (basic type, semantic type, label) for every column. This tells if the value is VALID/INVALID/NULL
count_file_pattern = 'col{}_count.txt' # Save for each row a tuple (basic type, semantic type, label, count) for each column 

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


## Aggregate and count the label for each column. Each row is assigned the count (last column) for the label (second last column): (basic_type, semantic_type, label, count)

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
