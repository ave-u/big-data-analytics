'''
    # Date Clean Script
    # 
'''
from pyspark import SparkContext
import datetime
from csv import reader

if __name__ == "__main__":
    sc = SparkContext()
    filepath    = '/user/xs741/NYPD_Complaint_Data_Historic.csv'
    df = sc.textFile(filepath).map(lambda l: reader([l]).__next__())
    header = df.first() # csv header
    df = df.filter(lambda line: line != header).cache() # filter out header

    '''
        # col 2 clean and format
        1. remove null rows
        2. replace 1015 year to year 2015
        3. keep only from 2006.01.01 - 2015.12.31 data
        4. change col2 into datetime format
    '''
    def cleanCol2(array):
        array[1] = datetime.datetime.strptime(array[1], '%m/%d/%Y')
        return array

    col2Cleaned = df \
        .filter(lambda array: array[1] != '') \
        .map(cleanCol2) \
        .filter(lambda array: array[1].year >= 2006 and array[1].year <= 2015)

    '''
        # col 3 clean and format
        1. keep null rows
        2. replace 24:00:00 change it into 00:00:00
           and also set a day forward in col 2
        3. change col3 into datetime time format
    '''
    def cleanCol3(array):
        if array[2] != '':
            if array[2] == '24:00:00':
                array[1] + datetime.timedelta(days=1)
                array[2] = '00:00:00'
            array[2] = datetime.datetime.strptime(array[2], '%H:%M:%S').time()
        return array

    col3Cleaned = col2Cleaned \
        .map(cleanCol3)

    '''
        # col 4 clean and format
        1. keep null rows
        2. replace 2090 year to 2009 year
        3. change col 4 to datetime date format
    '''
    def cleanCol4(array):
        array[3].replace('2090', '2009')
        if array[3] != '':
            array[3] = datetime.datetime.strptime(array[3], '%m/%d/%Y')
        return array

    col4Cleaned = col3Cleaned \
        .map(cleanCol4)

    '''
        # col 5 clean and format
        1. keep all null rows
        2. replace 24:00:00 to 00:00:00
           and also set a day forward in col 4
        3. change col5 into datetime time format
    '''
    def cleanCol5(array):
        if array[4] != '':
            if array[4] == '24:00:00':
                array[3] + datetime.timedelta(days=1)
                array[4] = '00:00:00'
            array[4] = datetime.datetime.strptime(array[4], '%H:%M:%S').time()
        return array

    col5Cleaned = col4Cleaned \
        .map(cleanCol5)

    '''
        # col 6
        We do not care col 6 because it is replicated with col2 and col4
    '''

    '''
        # col 14
        We do not need to change type of col 14 and keep null rows
        No Invalid data
    '''

    '''
        # col 15
        We do not need to change type of col 14 and keep null rows
        No Invalid data
    '''

    sc.stop()
