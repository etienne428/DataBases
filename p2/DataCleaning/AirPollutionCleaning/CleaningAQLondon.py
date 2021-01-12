import pandas as pd
import numpy as np
import AirPollutionCleaning.PollutantDictionary as polD

pathFarrington = 'Resources\London Farrington Street AQ.csv'
pathUpperThames = 'Resources\London Upper Thames Street.csv'
pathWalbrook = 'Resources\London Walbrook Whraf AQ.csv'
pathBeechStreet = 'Resources\London BeechStreet AQ.csv'


class cleanAQLondon:

    def __init__(self):
        self.Farrington = pd.read_csv(pathFarrington).replace('', np.nan)
        self.UpperThames = pd.read_csv(pathUpperThames).replace('', np.nan)
        self.BeechStreet = pd.read_csv(pathBeechStreet).replace('', np.nan)
        self.Walbrook = pd.read_csv(pathWalbrook).replace('', np.nan)
        self.dict = {'SO2': 2.6647, 'NO': 1.2741, 'NO2': 1.9123, 'CO': 1.1640 * 1000, 'O3': 1.9954}

    def cleanFarrington(self):
        datelist = []
        timelist = []
        SiteList = []
        SpeciesList = []
        ValueList = []


        for index, row in self.Farrington.dropna().iterrows():
            dateTime = row['ReadingDateTime']
            time = dateTime[11:13] + dateTime[14:16]
            date = str(dateTime[0:10]).replace('/', '-')
            SiteList.append('FarringtonStreet')
            SpeciesList.append(row['Species'])
            ValueList.append(row['Value'])
            datelist.append(date)
            timelist.append(time)

        toRet = pd.DataFrame()

        toRet['Location'] = ['London'] * len(self.Farrington.dropna())
        toRet['Date'] = datelist
        toRet['Time'] = timelist

        toRet['Site Code'] = SiteList
        toRet['Species'] = SpeciesList
        toRet['Value in µg/m³'] = ValueList
        toRet['Longitude'] = "-1"
        toRet['Latitude'] = "-1"



        return toRet

    def cleanUpperThames(self):
        datelist = []
        timelist = []
        SiteList = []
        SpeciesList = []
        ValueList = []

        for index, row in self.UpperThames.dropna().iterrows():
            dateTime = row['ReadingDateTime']
            time = dateTime[11:13] + dateTime[14:16]
            date = str(dateTime[0:10]).replace('/', '-')
            SiteList.append(row['Site'])
            SpeciesList.append('UpperThamesStreet')
            ValueList.append(row['Value'])
            datelist.append(date)
            timelist.append(time)

        toRet = pd.DataFrame()

        toRet['Location'] = ['London'] * len(self.UpperThames.dropna())
        toRet['Date'] = datelist
        toRet['Time'] = timelist

        toRet['Site Code'] = SiteList
        toRet['Species'] = SpeciesList
        toRet['Value in µg/m³'] = ValueList
        toRet['Longitude'] = "-1"
        toRet['Latitude'] = "-1"

        return toRet

    def cleanwalbrookWhraf(self):
        datelist = []
        timelist = []
        SiteList = []
        SpeciesList = []
        ValueList = []

        for index, row in self.Walbrook.dropna().iterrows():
            dateTime = row['ReadingDateTime']
            time = dateTime[11:13] + dateTime[14:16]
            date = str(dateTime[0:10]).replace('/', '-')
            SiteList.append('WalbrookWhraf')
            SpeciesList.append(row['Species'])
            ValueList.append(row['Value'])
            datelist.append(date)
            timelist.append(time)

        toRet = pd.DataFrame()

        toRet['Location'] = ['London'] * len(self.Walbrook.dropna())
        toRet['Date'] = datelist
        toRet['Time'] = timelist

        toRet['Site Code'] = SiteList
        toRet['Species'] = SpeciesList
        toRet['Value in µg/m³'] = ValueList
        toRet['Longitude'] = "-1"
        toRet['Latitude'] = "-1"

        return toRet

    def cleanBeechStreet(self):
        datelist = []
        timelist = []
        SiteList = []
        SpeciesList = []
        ValueList = []

        for index, row in self.BeechStreet.dropna().iterrows():
            dateTime = row['ReadingDateTime']
            time = dateTime[11:13] + dateTime[14:16]
            date = str(dateTime[0:10]).replace('/', '-')
            SiteList.append('BeechStreet')
            SpeciesList.append(row['Species'])
            ValueList.append(row['Value'])
            datelist.append(date)
            timelist.append(time)

        toRet = pd.DataFrame()

        toRet['Location'] = ['London'] * len(self.BeechStreet.dropna())
        toRet['Date'] = datelist
        toRet['Time'] = timelist

        toRet['Site Code'] = SiteList
        toRet['Species'] = SpeciesList
        toRet['Value in µg/m³'] = ValueList
        toRet['Longitude'] = "-1"
        toRet['Latitude'] = "-1"

        return toRet

    def runner(self):
        a = self.cleanFarrington()
        b = self.cleanBeechStreet()
        c = self.cleanUpperThames()
        d = self.cleanwalbrookWhraf()

        x = pd.concat([a,b,c,d], ignore_index=True)
        x.to_csv('Resources\cleaned_London.csv', index=False)









if __name__ == "__main__":

    aq = cleanAQLondon()
    aq.runner()



















