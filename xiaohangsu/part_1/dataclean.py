#from pyspark import SparkContext
from pyspark.sql.types import *
import datetime
from csv import reader
# sc = SparkContext()

filepath    = r'./NYPD_Complaint_Data_Historic.csv'
df = sc.textFile(filepath).map(lambda l: reader([l]).__next__())

header = df.first() # csv header

df = df.filter(lambda line: line != header).cache() # filter out header

def transform(array):
	array[1] = datetime.datetime.strptime(array[1], '%m/%d/%Y')
	return array

#replace year 1015
def replaceYear2015to2015(array):
	array[1] = array[1].replace('1015', '2015')
	return array

t = df \
	.filter(lambda array: array[1] != '') \
	.map(replaceYear2015to2015) \
	.map(transform) \
	.filter(lambda array: (array[1].year >= 2006 and array[1].year <= 2015))
print('Column 2 number: ', col2.count())


