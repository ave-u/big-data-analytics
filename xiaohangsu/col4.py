from pyspark import SparkContext
import datetime
from csv import reader

if __name__ == "__main__":
    sc = SparkContext()

    filepath    = r'/user/xs741/NYPD_Complaint_Data_Historic.csv'
    df = sc.textFile(filepath).map(lambda l: reader([l]).__next__())

    header = df.first() # csv header

    df = df.filter(lambda line: line != header).cache() # filter out header


    # column 4: CMPLNT_TO_DT
    # type    : datetime date
    # Format  : mm/dd/yyyy

    col4 = df \
        .map(lambda array: (array[3] if  array[3] != '' else None)) \
        .map(lambda x: x.replace('2090', '2009') if x != None else None) # data correct
    print('Column 4 number: ', col4.count())

    # null in Column 4
    nullCol4 = col4.filter(lambda date: date == None)
    print('Null column 4 number: ', nullCol4.count())

    # Invalid Date
    validCol4 = col4.filter(lambda date: date != None).map(lambda s: datetime.datetime.strptime(s, '%m/%d/%Y'))
    print('Invalid column 4 number: ', col4.count() - nullCol4.count() - validCol4.count())

    # Map Reduce by year
    year = validCol4 \
        .map(lambda x: (x.year, 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .sortBy(lambda x: x[0])
    year.collect()

    # Map Reduce by month
    month = validCol4 \
        .map(lambda x: (x.month, 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .sortBy(lambda x: x[0])
    month.collect()

    # Map Reduce by day
    day = validCol4 \
        .map(lambda x: (x.day, 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .sortBy(lambda x: x[0])
    day.collect()

    col4 \
        .map(lambda x: x + ' DATE END_DATE VALID' if x != None else 'NULL') \
        .saveAsTextFile('col4.out')

    sc.stop()
