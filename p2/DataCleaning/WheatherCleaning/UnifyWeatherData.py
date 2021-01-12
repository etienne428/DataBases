import pandas as pd

pathBasel = 'Resources\weather basel cleaned.csv'
pathLA = 'Resources\weather LA cleaned.csv'
pathLondon = 'Resources\weather London cleaned.csv'

"""
Class unifyWeather serves the purpose of combining the cleaned
weather files into a cleaned and integrateable csv file
"""

class unifiyWeather():

    def __init__(self):
        self.pd = self.concatenateWeather()
        self.saveCleaned(self.pd)
    #ConcateNate cleaned files
    def concatenateWeather(self):
        basel = pd.read_csv(pathBasel, dtype=str)
        la = pd.read_csv(pathLA, dtype=str)
        london = pd.read_csv(pathLondon, dtype=str)
        pdCombined = pd.concat([basel, la, london], ignore_index=True)
        return pdCombined
    #Save the combined files to the path specified
    def saveCleaned(self, dataframe):
        dataframe.to_csv('Resources\weather cleaned.csv', index=False)

if __name__ == '__main__':
    a = unifiyWeather()
