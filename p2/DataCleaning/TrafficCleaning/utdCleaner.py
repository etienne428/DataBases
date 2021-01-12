
import multiprocessing as mp
import tqdm
from multiprocessing import Pool
import pandas as pd

num_processes = mp.cpu_count()
path = 'Resources\ethutd19.csv'

TimeDictionary = {             range(0, 3600): "0000",
                               range(3600, 7200): "0100",
                               range(7200, 10800): "0200",
                               range(10800, 14400): "0300",
                               range(14400, 18000): "0400",
                               range(18000, 21600): "0500",
                               range(21600, 25200): "0600",
                               range(25200, 28800): "0700",
                               range(28800, 32400): "0800",
                               range(32400, 36000): "0900",
                               range(36000, 39600): "1000",
                               range(39600, 43200): "1100",
                               range(43200, 46800): "1200",
                               range(46800, 50400): "1300",
                               range(50400, 54000): "1400",
                               range(54000, 57600): "1500",
                               range(57600, 61200): "1600",
                               range(61200, 64800): "1700",
                               range(64800, 68400): "1800",
                               range(68400, 72000): "1900",
                               range(72000, 75600): "2000",
                               range(75600, 79200): "2100",
                               range(79200, 82800): "2200",
                               range(82800, 90000): "2300"

                             }

"""
This class serves the purpose of cleaning the utd Dataset.
"""

class utdCleaner:

    def __init__(self):
        self.df = pd.read_csv(path, chunksize=(10**5), low_memory=True)
        self.toRet = pd.DataFrame()


    #Process the data
    def process_rows(x:pd.DataFrame):
        timelist = []
        dayList = []
        cityList = []
        for day, interval, city in zip(x['day'], x['interval'], x['city']):
            #Map the interval to the correct time
            for key in TimeDictionary:
                if(int(interval) in key):
                    timelist.append(TimeDictionary[key])
            #the the date into the correct format
            dayList.append(day[8:10] + '-' + day[5:7]+ '-' + day[0:4])

            #Clean City Names
            if (city=='basel'):
                cityList.append('Basel')
            elif(city == 'losangeles'):
                cityList.append('Los Angeles')
            elif(city == 'london'):
                cityList.append('London')
            else:
                cityList.append(city)



        # Set day as key and dayList as value of Dataframe
        x['day'] = dayList
        # Set Time as key and timeList as value of Dataframe
        x['Time'] = timelist

        # Set city as key and citylist as value of Dataframe
        x['city'] = cityList

        #return the altered dataframe
        return x






if __name__ == '__main__':


    a = utdCleaner()

    #Use Multiprocessing on 8 cores
    num_partitions = num_processes
    pool = Pool(num_partitions)
    toRet = pd.DataFrame()
    for chunk in a.df:
        for x in tqdm.tqdm(pool.map(utdCleaner.process_rows, [chunk]), total = num_partitions):
            x.to_csv('Resources\ETHTrafficCleaned.csv', mode='a', index=False)
    pool.close()
    pool.join()




