from pyspark import SparkContext
from csv import reader

if __name__ == "__main__":

    sc = SparkContext()

    filepath    = r'/user/xs741/NYPD_Complaint_Data_Historic.csv'
    df = sc.textFile(filepath).map(lambda l: reader([l]).__next__())

    header = df.first() # csv header

    df = df.filter(lambda line: line != header).cache() # filter out header


    # Column 1: CMPLNT_NUM
    # Type    : INT
    # Format  : Big Integer

    persistentId = df.map(lambda array: (int(array[0]) if array[0] != '' else None))
    print('Persistent id number; ', persistentId.count())

    # null count for persistentId
    nullPersistentId = persistentId.filter(lambda id: id == None)
    print('Null persistent id number: ', nullPersistentId.count())

    # for persistentId should be unique, checking if persistentId is unique
    uniquePersistentId = persistentId.distinct()
    print('Duplicate persistent id number: ', persistentId.count() - uniquePersistentId.count())

    # range of Persistent Id
    print('Persistent Id range from: ', persistentId.min(),
        ' to ', persistentId.max())

    persistentId \
        .map(lambda x: str(x) + ' INT VALID' if x != None else 'NULL') \
        .saveAsTextFile('col1.out')
    sc.stop()