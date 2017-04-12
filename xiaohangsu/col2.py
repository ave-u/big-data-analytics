#from pyspark import SparkContext
from pyspark.sql.types import *
import datetime
from csv import reader
# sc = SparkContext()

filepath    = r'./NYPD_Complaint_Data_Historic.csv'
df = sc.textFile(filepath).map(lambda l: reader([l]).__next__())

header = df.first() # csv header

df = df.filter(lambda line: line != header).cache() # filter out header


# column 2: CMPLNT_FR_DT
# type    : datetime date
# Format  : mm/dd/yyyy

col2 = df.map(lambda array: (array[1] if array[1] != '' else None))
print('Column 2 number: ', col2.count())

# null in Column 2
nullCol2 = col2.filter(lambda date: date == None)
print('Null column 2 number: ', nullCol2.count())

# Invalid Date
validCol2 = col2.filter(lambda date: date != None).map(lambda s: datetime.datetime.strptime(s, '%m/%d/%Y'))
print('Invalid column 2 number: ', col2.count() - nullCol2.count() - validCol2.count())

# Map Reduce by year
year = validCol2 \
    .map(lambda x: (x.year, 1)) \
    .reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda x: x[0])
year.collect()

# Map Reduce by month
month = validCol2 \
    .map(lambda x: (x.month, 1)) \
    .reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda x: x[0])
month.collect()

# Map Reduce by day
day = validCol2 \
    .map(lambda x: (x.day, 1)) \
    .reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda x: x[0])
day.collect()