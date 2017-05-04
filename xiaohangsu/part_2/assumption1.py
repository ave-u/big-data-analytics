from pyspark import SparkContext
import datetime
from csv import reader

if __name__ == "__main__":

    sc = SparkContext()
    # use dataclean.py from here to clean data
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

    dateCount = t \
        .map(lambda array: (str(array[1].month) + '/' + str(array[1].day), 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .sortBy(lambda x: x[1]) \
        .saveAsTextFile('assumption1.out')

    sc.stop()