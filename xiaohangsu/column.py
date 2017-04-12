#from pyspark import SparkContext
from pyspark.sql.types import *
import datetime
from csv import reader
# sc = SparkContext()

filepath 	= r'./NYPD_Complaint_Data_Historic.csv'
df = sc.textFile(filepath).map(lambda l: reader([l]).__next__())

header = df.first() # csv header

df = df.filter(lambda line: line != header).cache() # filter out header

count = df.filter(lambda l: len(l) == 24)
# persistentId

persistentId = df.map(lambda array: (int(array[0]) if array[0] != '' else None))
print('Persistent id number; ', persistentId.count())
# null count for persistentId
nullPersistentId = df.filter(lambda id: id == None)
print('Null persistent id number: ', nullPersistentId.count())

# for persistentId should be unique, checking if persistentId is unique
uniquePersistentId = persistentId.distinct()
print('Duplicate persistent id number: ', persistentId.count() - uniquePersistentId.count())

# df = df.map(lambda array: [
# 	(int(array[0]) if array[0] != '' else None),
# 	(datetime.datetime.strptime(array[1], '%m/%d/%y') if array[1] != '' else None),
# 	(datetime.datetime.strptime(array[2], '%H:%M:%S') if array[2] != '' else None),
# 	(datetime.datetime.strptime(array[3], '%m/%d/%y') if array[3] != '' else None),
# 	(datetime.datetime.strptime(array[4], '%H:%M:%S') if array[2] != '' else None),
# 	str(array[5]),
# 	(int(array[6]) if array[6] != '' else None),
# 	str(array[7]),
# 	(int(array[8]) if array[8] != '' else None),
# 	str(array[9]), str(array[10]), str(array[11]),
# 	str(array[12]), str(array[13]),
# 	(int(array[14]) if array[14] != '' else None),
# 	str(array[15]), str(array[16]), str(array[17]),
# 	str(array[18]), str(array[19]), str(array[20]),
# 	(float(array[21]) if array[21] != '' else None),
# 	(float(array[22]) if array[22] != '' else None),
# 	str(array[23])
# 	])



schema = StructType([
	StructField('CMPLNT_NUM', IntegerType(), nullable=True),
	StructField('CMPLNT_FR_DT', StringType(), nullable=True),
	StructField('CMPLNT_FR_TM', DateType(), nullable=True),
	StructField('CMPLNT_TO_DT', DateType(), nullable=True),
	StructField('CMPLNT_TO_TM', DateType(), nullable=True),
	StructField('RPT_DT', StringType(), nullable=True),
	StructField('KY_CD', IntegerType(), nullable=True),
	StructField('OFNS_DESC', StringType(), nullable=True),
	StructField('PD_CD', IntegerType(), nullable=True),
	StructField('PD_DESC', StringType(), nullable=True),
	StructField('CRM_ATPT_CPTD_CD', StringType(), nullable=True),
	StructField('LAW_CAT_CD', StringType(), nullable=True),
	StructField('JURIS_DESC', StringType(), nullable=True),
	StructField('BORO_NM', StringType(), nullable=True),
	StructField('ADDR_PCT_CD', IntegerType(), nullable=True),
	StructField('LOC_OF_OCCUR_DESC', StringType(), nullable=True),
	StructField('PREM_TYP_DESC', StringType(), nullable=True),
	StructField('PARKS_NM', StringType(), nullable=True),
	StructField('HADEVELOPT', StringType(), nullable=True),
	StructField('X_COORD_CD', StringType(), nullable=True),
	StructField('Y_COORD_CD', StringType(), nullable=True),
	StructField('Latitude', DoubleType(), nullable=True),
	StructField('Longitude', DoubleType(), nullable=True),
	StructField('Lat_Lon', StringType(), nullable=True)])

dataFrame = spark.createDataFrame(df, schema).cache()