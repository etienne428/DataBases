import pandas as pd
import AirPollutionCleaning.PollutantDictionary as polD

Chrischona = 'Resources\Chrischona_Luftqualität.csv'
Feldbergstrasse = 'Resources\Feldbergstrasse_Luftqualität.csv'
StJohannsplatz = 'Resources\St_Johannsplatz_Luftqualität.csv'

class cleanAQBasel:

    def __init__(self):
        self.dict = {'SO2': 2.6647, 'NO': 1.2741, 'NO2': 1.9123, 'CO': 1.1640 * 1000, 'O3': 1.9954}
        self.Chrischona = pd.read_csv(Chrischona, delimiter=';')
        with open(Feldbergstrasse) as f:
            print(f)
        self.Feldbergstrasse = pd.read_csv(Feldbergstrasse, delimiter=';', encoding='cp1252')
        self.StJohannsplatz = pd.read_csv(StJohannsplatz, delimiter=';', encoding='cp1252')


    def cleanChrischona(self):
        toRet = pd.DataFrame()

        dateList = []
        timeList = []
        Latitude = []
        longiTude = []
        Location = []
        for index, row in self.Chrischona.iterrows():
            date = row['Datum/Zeit']
            coordinates = row['geo_point_2d'].split(',')

            dateList.append(date[8:10] + '-' + date[5:7] + '-' + date[0:4])
            timeList.append(date[11:13]+date[14:16])
            Latitude.append(coordinates[0])
            longiTude.append(coordinates[1])
            Location.append('Basel')


        toRet['Location'] = Location
        toRet['Date'] = dateList
        toRet['Time'] = timeList

        toRet['Site Code'] = 'Chrischona'
        toRet['Species'] = 'O3'
        toRet['Value in µg/m³'] = self.Chrischona['O3 (Stundenmittelwerte [µg/m³])']
        toRet['Longitude'] = longiTude
        toRet['Latitude'] = Latitude

        return toRet

    def cleanFeldbergstrasse(self):
        toRet = pd.DataFrame()

        dateList = []
        timeList = []
        Latitude = []
        longiTude = []
        Location = []
        SpeciesList = []
        ValueList = []

        Species = ['PM10 (Stundenmittelwerte [µg/m³])','PM2.5 (Stundenmittelwerte [µg/m³])', 'NO2 (Stundenmittelwerte [µg/m³])']
        Name = ['PM10', 'PM2.5', 'NO2']

        for species, name in zip(Species, Name):
            for index, row in self.Feldbergstrasse.dropna().iterrows():
                date = row['Datum/Zeit']
                coordinates = row['geo_point_2d'].split(',')
                SpeciesList.append(name)
                ValueList.append(row[species])



                dateList.append(date[8:10] + '-' + date[5:7] + '-' + date[0:4])
                timeList.append(date[11:13]+date[14:16])
                Latitude.append(coordinates[0])
                longiTude.append(coordinates[1])
                Location.append('Basel')


        toRet['Location'] = Location
        toRet['Date'] = dateList
        toRet['Time'] = timeList

        toRet['Site Code'] = 'Feldbergstrasse'
        toRet['Species'] = SpeciesList
        toRet['Value in µg/m³'] = ValueList
        toRet['Longitude'] = longiTude
        toRet['Latitude'] = Latitude



        return toRet

    def cleanStJohannsplatz(self):
        toRet = pd.DataFrame()

        dateList = []
        timeList = []
        Latitude = []
        longiTude = []
        Location = []
        SpeciesList = []
        ValueList = []

        Species = ['PM10 (Stundenmittelwerte [µg/m³])', 'PM2.5 (Stundenmittelwerte [µg/m³])',
                   'O3 (Stundenmittelwerte [µg/m³])']
        Name = ['PM10', 'PM2.5', '03']

        for species, name in zip(Species, Name):
            for index, row in self.StJohannsplatz.dropna().iterrows():
                date = row['Datum/Zeit']
                coordinates = row['geo_point_2d'].split(',')
                SpeciesList.append(name)
                ValueList.append(row[species])

                dateList.append(date[8:10] + '-' + date[5:7] + '-' + date[0:4])
                timeList.append(date[11:13] + date[14:16])
                Latitude.append(coordinates[0])
                longiTude.append(coordinates[1])
                Location.append('Basel')

        toRet['Location'] = Location
        toRet['Date'] = dateList
        toRet['Time'] = timeList

        toRet['Site Code'] = 'StJohannsplatz'
        toRet['Species'] = SpeciesList
        toRet['Value in µg/m³'] = ValueList
        toRet['Longitude'] = longiTude
        toRet['Latitude'] = Latitude

        return toRet



    def concatenateAndSaveSites(self):
        a = self.cleanChrischona()
        b = self.cleanStJohannsplatz()
        c = self.cleanFeldbergstrasse()

        toSave = pd.concat([a,b,c], ignore_index=True)
        toSave.to_csv('Resources\cleanedBasel.csv', index=False)





if __name__ == "__main__":

    aq = cleanAQBasel()
    aq.concatenateAndSaveSites()









