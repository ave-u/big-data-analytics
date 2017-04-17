from pyspark import SparkContext
import datetime
from csv import reader

if __name__ == "__main__":

    sc = SparkContext()
    filepath    = r'./NYPD_Complaint_Data_Historic.csv'
    df = sc.textFile(filepath).map(lambda l: reader([l]).__next__())

    header = df.first() # csv header

    df = df.filter(lambda line: line != header).cache() # filter out header


    # column 14: BORO_NM
    # type    : Plain Text
    # Format  : Borough five possible value

    col14 = df.map(lambda array: (array[13] if array[13] != '' else None))
    print('Column 14 number: ', col14.count())

    # null in col14
    nullCol14 = col14.filter(lambda borough: borough == None)
    print('Column 14 null number: ', nullCol14.count())

    # Map Reduce by Value
    borough = col14 \
        .filter(lambda borough: borough != None) \
        .map(lambda borough: (borough, 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .sortBy(lambda x: x[0])
    borough.collect()

    col14 \
        .map(lambda x: x + ' TEXT VALID' if x != None else 'NULL') \
        .saveAsTextFile('col14.out')

    borough \
        .saveAsTextFile('col14_borough.out')

    sc.stop()