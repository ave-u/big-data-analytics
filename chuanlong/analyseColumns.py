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

# Format the column, output the item as required
def format(df, col_num, col_name, attr_type, valid_func):
	# format the data
	attr = df.map(lambda x: x[col_num])\
			 .map(lambda x: (x, valid_func(x)))\
			 .map(lambda x: '%s\t%s\t%s\t%s' % (x[0], attr_type, col_name, x[1]))
	output_filepath = col_name + '.out'
	attr.saveAsTextFile(output_filepath)
	return attr

# Output the very basic summary of the column, such as: Number of Valid rows, Invalid rows and Null rows and write them into a .txt file
def summary(attr, attr_name, summary_file):
	lines = []
	line1 = "Attribute:\t" + str(attr_name) + '\n'
	lines += [line1]

	attr = attr.map(lambda x: x.split('\t'))\
			   .map(lambda x: (x[0], x[3]))

	valid_data = attr.filter(lambda x: x[1] == "VALID")
	valid_data_num = valid_data.count()
	line2 = "Number of VALID Rows:\t" + str(valid_data_num) + '\n'
	lines += [line2]

	valid_data = valid_data.map(lambda x: (x[0], 1))\
						   .reduceByKey(lambda x, y: x + y)\
						   .sortBy(lambda x: x[1], ascending = False).take(10)
	line6 = 'Examples of VALID Rows:\t' + str(valid_data) + '\n'
	lines += [line6]

	invalid_data = attr.filter(lambda x: x[1] == "INVALID")
	invalid_data_num = invalid_data.count()
	line3 = "Number of INVALID Rows:\t" + str(invalid_data_num) + '\n'
	lines += [line3]

	invalid_example = invalid_data.map(lambda x: x[0]).take(5)
	line4 = "Example of INVALID Rows and its frequency:\t" + str(invalid_example) + '\n'
	lines += [line4]

	null_data = attr.filter(lambda x: x[1] == "NULL")
	null_data_num = null_data.count()
	line5 = "Number of NULL Rows:\t" + str(null_data_num) + '\n'
	lines += [line5]

	for line in lines:
		summary_file.write(line)

	summary_file.write('\n')

# Main Function
if __name__ == '__main__':
	sc = SparkContext()
	# summary file
	try:
		summary_file = open('summary.txt', 'r')
	except:
		summary_file = open('summary.txt', 'w')

	# Load and read the dataset
	file_path = r"/user/xs741/NYPD_Complaint_Data_Historic.csv"
	# file_path = "sample.csv"
	df = sc.textFile(file_path)
	df = df.mapPartitions(lambda x : reader(x))

	# Skip the first row, which is head of the file
	header = df.first()
	df = df.filter(lambda x : x != header)

	# Test the dataset with small dataset
	#df = sc.parallelize(df.filter(lambda x: x!= header).take(1000))

	# Column: LOC_OF_OCCUR_DESC
	loc_of_occur_desc = format(df, 15, 'LOC_OF_OCCUR_DESC', 'TEXT', isValidText)
	summary(loc_of_occur_desc, 'LOC_OF_OCCUR_DESC', summary_file)

	# Column: PREM_TYP_DESC
	prem_typ_desc = format(df, 16, 'PREM_TYP_DESC', 'TEXT', isValidText)
	summary(prem_typ_desc, 'PREM_TYP_DESC', summary_file)

	# Column: PARKS_NM
	parks_nm = format(df, 17, 'PARKS_NM', 'TEXT', isValidText)
	summary(parks_nm, 'PARKS_NM', summary_file)

	# Column: HADEVELOPT
	hadevelopt = format(df, 18, 'HADEVELOPT', 'TEXT', isValidText)
	summary(hadevelopt, 'HADEVELOPT', summary_file)

	# Column: X_COORD_CD
	x_coord_cd = format(df, 19, 'X_COORD_CD', 'FLOAT', isValidCoords)
	summary(x_coord_cd, 'X_COORD_CD', summary_file)

	# Column: Y_COORD_CD
	y_coord_cd = format(df, 20, 'Y_COORD_CD', 'FLOAT', isValidCoords)
	summary(y_coord_cd, 'Y_COORD_CD', summary_file)

	# Column: Latitude
	latitude = format(df, 21, 'LATITUDE', 'FLOAT', isValidCoords)
	summary(latitude, 'LATITUDE', summary_file)

	# Column: Longitude
	longitude = format(df, 22, 'LONGITUDE', 'FLOAT', isValidCoords)
	summary(longitude, 'LONGITUDE', summary_file)

	summary_file.close()
	sc.stop()
