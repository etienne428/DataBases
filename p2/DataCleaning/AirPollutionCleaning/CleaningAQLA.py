import pandas as pd
import AirPollutionCleaning.PollutantDictionary as polD

pathSO2 = 'Resources\SO2_US_2017.csv'
pathNO2 = 'Resources\\NO2_US_2017.csv'
pathCO = 'Resources\CO_US_2017.csv'
pathO3 = 'Resources\O3_US_2017.csv'

class cleanAQLA:

    def __init__(self):
        self.dict = {'SO2': 2.6647, 'NO': 1.2741, 'NO2': 1.9123, 'CO': 1.1640 * 1000, 'O3': 1.9954}
        self.SO2 = pd.read_csv(pathSO2, low_memory=False)
        self.NO2 = pd.read_csv(pathNO2, low_memory=False)
        self.CO = pd.read_csv(pathCO, low_memory=False)
        self.O3 = pd.read_csv(pathO3, low_memory=False)
        self.df = pd.concat([self.SO2, self.NO2, self.CO, self.O3])

    def runner(self):
        speciesList = []
        dateList = []
        timeList = []
        valueList = []
        Site = []
        for index, row in self.df.iterrows():
            species = row['Parameter Name']
            timeList.append(row['Time Local'][0:2] + row['Time Local'][3:5])
            Site.append(row['Site Num'])

            dateLoc = row['Date Local']
            value = row['Sample Measurement']

            dateList.append(dateLoc[8:11] + "-" + dateLoc[5:7] + "-" + dateLoc[0:4])

            #Clean the species
            if (str(species).__contains__('Sulfur')):
                species = "SO2"
            elif (str(species).__contains__('Nitrogen')):
                species = "NO2"
            elif (str(species).__contains__("Carbon")):
                species = "CO"
            elif (str(species).__contains__("Ozone")):
                species = "O3"
            #Append the species to the species List
            speciesList.append(species)
            #get the correct factor of the pollutant dictionary
            valueList.append(self.dict.get(species) * value)

        toRet = pd.DataFrame()

        toRet['Location'] = self.df['County Name']
        toRet['Date'] = dateList
        toRet['Time'] = timeList

        toRet['Site Code'] = Site
        toRet['Species'] = speciesList
        toRet['Value in µg/m³'] = valueList
        toRet['Longitude'] = self.df['Longitude']
        toRet['Latitude'] = self.df['Latitude']

        toRet.to_csv('Resources\cleaned_LA.csv', index=False)

if __name__ == "__main__":

    aq = cleanAQLA()
    aq.runner()








