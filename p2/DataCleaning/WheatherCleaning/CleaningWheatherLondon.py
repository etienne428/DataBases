import pandas as pd

path = 'Resources\weather_data_1hr London.csv'


class cleanWeatherLondon:

    def __init__(self):
        self.data = pd.read_csv(path)

    def saveCleaned(self, dataframe):
        dataframe.to_csv('Resources\weather London cleaned.csv')

    def runner(self):
        toRet = pd.DataFrame()

        listDate = []
        listTime = []
        # iterate through data rows
        for i in range(len(a.data)):
            # Get date into correct format
            date = str(self.data.iloc[i, 1])[8:10] + "-" + str(self.data.iloc[i, 1])[5:7] + "-" + str(
                self.data.iloc[i, 1])[0:4]
            # extract time
            time = str(self.data.iloc[i, 2])
            listDate.append(date)
            # Clean time
            if (len(time) == 1):
                x = "0000"
                listTime.append(x)
            elif (len(time) == 3):
                x = "0" + time
                listTime.append(x)
            else:
                listTime.append(time)

        toRet['Date'] = listDate
        toRet['Time'] = listTime
        toRet['Location'] = 'London'
        toRet['Temperature'] = self.data['tempC']
        toRet['Wind Speed'] = self.data['windspeedKmph']
        toRet['Precipitation'] = self.data['precipMM']
        toRet['Relative Humidity'] = self.data['humidity']
        toRet['Wind Direction'] = self.data['winddirdegree']
        toRet['Air Pressure'] = self.data['pressureMB']
        toRet['Cloud Coverage'] = self.data['cloudcover']

        toRet['Time'].apply(str)

        self.saveCleaned(toRet)


if __name__ == '__main__':
    a = cleanWeatherLondon()
    a.runner()
