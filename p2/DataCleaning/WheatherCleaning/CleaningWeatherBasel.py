import pandas as pd

path = "Resources\weather_basel.csv"
class cleanWheatherBasel:


    #Read Data from csv file
    def __init__(self):
        self.data = pd.read_csv(path)
    #Save dataframe to csv
    def saveCleaned(self, dataframe):
        dataframe.to_csv('Resources\weather_basel_cleaned.csv')
    #Data Cleaning
    def runner(self):
        toRet = pd.DataFrame()

        listDate = []
        listTime = []
        #Iterate through the rows of the datawframe
        for i in range(len(a.data)):

            #Get the date in to the correct format
            date = str(self.data.iloc[i, 0])[6:8] + "-" + str(self.data.iloc[i, 0])[4:6] + "-" + str(self.data.iloc[i, 0])[0:4]
            #Get the time variable
            time = str(self.data.iloc[i, 0][9:13])
            #Appending to the corresponding list
            listTime.append(time)
            listDate.append(date)

        toRet['Date'] = listDate
        toRet['Time'] = listTime
        toRet['Location'] = 'Basel'
        toRet['Temperature'] = self.data['Basel Temperature [2 m elevation corrected]']
        toRet['Wind Speed'] = self.data['Basel Wind Speed [10 m]']
        toRet['Precipitation'] = self.data['Basel Precipitation Total']
        toRet['Relative Humidity'] = self.data['Basel Relative Humidity [2 m]']
        toRet['Wind Direction'] = self.data['Basel Wind Direction [10 m]']
        toRet['Air Pressure'] = self.data['Basel Mean Sea Level Pressure [MSL]']
        toRet['Cloud Coverage'] = self.data['Basel Cloud Cover Total']

        toRet['Time'].apply(str)

        #Save the cleaned Dataframe
        self.saveCleaned(toRet)


if __name__ == "__main__":
    a = cleanWheatherBasel()
    a.runner()






