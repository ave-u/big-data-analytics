#from pyspark import SparkContext
from pyspark.sql.types import *
import datetime
from csv import reader
# sc = SparkContext()

filepath    = r'./NYPD_Complaint_Data_Historic.csv'
df = sc.textFile(filepath).map(lambda l: reader([l]).__next__())

header = df.first() # csv header

df = df.filter(lambda line: line != header).cache() # filter out header


# column 6: RPT_DT
# type    : datetime date
# Format  : mm/dd/yyyy

col6 = df.map(lambda array: (array[5] if  array[5] != '' else None))
print('Column 6 number: ', col6.count())

# null in Column 6
nullCol6 = col6.filter(lambda date: date == None)
print('Null column 6 number: ', nullCol6.count())

# Invalid Date
validCol6 = col6.filter(lambda date: date != None).map(lambda s: datetime.datetime.strptime(s, '%m/%d/%Y'))
print('Invalid column 6 number: ', col6.count() - nullCol6.count() - validCol6.count())

# Map Reduce by year
year = validCol6 \
    .map(lambda x: (x.year, 1)) \
    .reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda x: x[0])
year.collect()

# Map Reduce by month
month = validCol6 \
    .map(lambda x: (x.month, 1)) \
    .reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda x: x[0])
month.collect()

# Map Reduce by day
day = validCol6 \
    .map(lambda x: (x.day, 1)) \
    .reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda x: x[0])
day.collect()
