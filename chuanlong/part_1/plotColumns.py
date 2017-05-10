from __future__ import print_function
from pyspark import SparkContext
from csv import reader
import sys

# Validate the text value
def isValidText(x):
	if x == '':
		return 'NULL'
	if type(x) == str:
		x = x.strip()
		return 'VALID' if len(x) > 0 else 'INVALID'
	else:
		return 'INVALID'

# Validate the coorinate value 
def isValidCoords(x):
	if x == '':
		return 'NULL'
	try:
		x = float(x)
		return 'VALID'
	except:
		return 'INVALID'

def validate(attrs):
	if isValidText(attrs[0]) == 'NULL' and isValidText(attrs[1]) == 'NULL' and isValidText(attrs[2]) == 'NULL' \
	and isValidText(attrs[3]) == 'NULL' and isValidCoords(attrs[4]) == 'NULL' and isValidCoords(attrs[5]) == 'NULL' \
	and isValidCoords(attrs[6]) == 'NULL' and isValidCoords(attrs[7]) == 'NULL':
		return False
	else:
		return True

# Main Function
if __name__ == '__main__':
	sc = SparkContext()

	# Load and read the dataset
	file_path = r"/user/xs741/NYPD_Complaint_Data_Historic.csv"

	df = sc.textFile(file_path)
	df = df.mapPartitions(lambda x : reader(x))

	# Skip the first row, which is head of the file
	header = df.first()
	df = df.filter(lambda x : x != header)

	# Test the script with small dataset
	# df = sc.parallelize(df.filter(lambda x: x!= header).take(500))

	df = df.map(lambda x: (x[15], x[16], x[17], x[18], x[19], x[20], x[21], x[22]))\
		   .filter(lambda x: validate(x) == True)\
		   .map(lambda x: '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]))\
		   .saveAsTextFile('columns.out')
	sc.stop()
