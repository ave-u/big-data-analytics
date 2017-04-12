#from pyspark import SparkContext
from pyspark.sql.types import *
import datetime
from csv import reader
# sc = SparkContext()

filepath    = r'./NYPD_Complaint_Data_Historic.csv'
df = sc.textFile(filepath).map(lambda l: reader([l]).__next__())

header = df.first() # csv header

df = df.filter(lambda line: line != header).cache() # filter out header


# column 15: ADDR_PCT_CD
# type    : Number
# Format  : 

col15 = df.map(lambda array: (array[14] if array[14] != '' else None))
print('Column 15 number: ', col15.count())

# null in col15
nullCol15 = col15.filter(lambda id: id == None)
print('Column 15 null number: ', nullCol15.count())

# Map Reduce by Value
id = col15 \
    .filter(lambda id: id != None) \
    .map(lambda id: (int(id), 1)) \
    .reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda x: x[0])
id.collect()