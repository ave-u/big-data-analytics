from pyspark import SparkContext
import datetime
from csv import reader

if __name__ == "__main__":

    sc = SparkContext()

    filepath    = r'/user/xs741/NYPD_Complaint_Data_Historic.csv'
    df = sc.textFile(filepath).map(lambda l: reader([l]).__next__())

    header = df.first() # csv header

    df = df.filter(lambda line: line != header).cache() # filter out header


    # column 3: CMPLNT_FR_TM
    # type    : datetime time
    # Format  : HH:MM:SS

    col3 = df.map(lambda array: (array[2] if  array[2] != '' else None))
    print('Column 3 number: ', col3.count())

    # null in Column 3
    nullCol3 = col3.filter(lambda date: date == None)
    print('Null column 3 number: ', nullCol3.count())

    # Invalid Date
    def invalid(s):
        try:
            datetime.datetime.strptime(s, '%H:%M:%S').time()
            return False
        except:
            return True

    inValidCol3 = col3 \
        .filter(lambda date: date != None) \
        .filter(invalid)
    print('Invalid column 3 number: ', inValidCol3.count())

    # Invalid data 24:00:00 transform into 00:00:00
    def transform(s):
        try:
            return datetime.datetime.strptime(s, '%H:%M:%S').time()
        except:
            return datetime.datetime.strptime("00:00:00", '%H:%M:%S').time()

    validCol3 = col3 \
        .filter(lambda date: date != None) \
        .map(transform)

    # Map Reduce by hour
    hour = validCol3 \
        .map(lambda x: (x.hour, 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .sortBy(lambda x: x[0])
    hour.collect()

    # Map Reduce by minute
    minute = validCol3 \
        .map(lambda x: (x.minute, 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .sortBy(lambda x: x[0])
    minute.collect()

    # Map Reduce by second
    second = validCol3 \
        .map(lambda x: (x.second, 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .sortBy(lambda x: x[0])
    second.collect()

    col3 \
        .map(lambda x: x + ' TIME VALID' if x != None else 'NULL') \
        .saveAsTextFile('col3.out')

    sc.stop()
