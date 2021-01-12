import multiprocessing as mp
import tqdm
from multiprocessing import Pool
import pandas as pd

num_processes = mp.cpu_count()
path = 'Resources\converted_MIV.csv'

"""
This class is used in order to clean the MIV Dataset
"""
class MVIClean:



    def __init__(self):
        self.length = len(path)

        self.df = pd.read_csv(path, chunksize=(10**5), low_memory=True, delimiter=';')
        self.toRet = pd.DataFrame()


    #Iterate through Data
    def process_rows(x:pd.DataFrame):


        timelist = []
        dayList = []

        toRet = pd.DataFrame()
        for index, row in x.iterrows():
            #Reformat Date
            day = row['Date'].replace('.', '-')
            #Reformat Time
            time = row['TimeFrom'][0:2] + row['TimeFrom'][3:5]


            dayList.append(day)
            timelist.append(time)
        #Set Location artificially
        toRet['Location'] = ['Basel'] *len(x)
        toRet['Site Code'] = x['SiteCode']
        toRet['Site Name'] = x['SiteName']
        toRet['Direction Name'] = x['DirectionName']
        toRet['Lane Code'] = x['LaneCode']
        toRet['LaneName'] = x['SiteCode']
        toRet['Date'] = dayList
        toRet['Time'] = timelist
        toRet['TrafficType'] = x['TrafficType']
        toRet['Total'] = x['Total']
        toRet['MR'] = x['MR']
        toRet['PW'] = x['PW']
        toRet['PW+'] = x['PW+']
        toRet['Lief'] = x['Lief']
        toRet['LW'] = x['LW']
        toRet['PW+'] = x['PW+']
        toRet['Sattelzug'] = x['Sattelzug']
        toRet['Bus'] = x['Bus']
        toRet['andere'] = x['andere']



        return toRet






if __name__ == '__main__':


    a = MVIClean()
    new_df = pd.DataFrame()
    #Run this code on eight cores for better performance
    num_partitions = num_processes
    pool = Pool(num_partitions)
    toRet = pd.DataFrame()
    for chunk in a.df:
        for x in tqdm.tqdm(pool.map(MVIClean.process_rows, [chunk]), total = num_partitions):
            x.drop_duplicates()
            x.to_csv('Resources\MVITrafficCleaned.csv', mode='a', index=False)
    pool.close()
    pool.join()
