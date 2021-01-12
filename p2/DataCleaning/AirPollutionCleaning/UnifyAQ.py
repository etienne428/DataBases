import pandas as pd
import numpy as np

pathBasel = 'Resources\cleanedBasel.csv'
pathLA = 'Resources\cleaned_LA.csv'
pathLondon = 'Resources\cleaned_London.csv'

"""
Class UnifyAQ serves the purpose of combining the cleaned
AQ files into a cleaned and integrateable csv file
"""

class UnifyAQ():

    def __init__(self):
        self.pd = self.concatenateWeather()
        self.saveCleaned(self.pd)
    #ConcateNate cleaned files
    def concatenateWeather(self):
        basel = pd.read_csv(pathBasel, dtype=str)
        la = pd.read_csv(pathLA, dtype=str)
        #london = pd.read_csv(pathLondon, dtype=str)
        pdCombined = pd.concat([basel, la]).replace('', np.nan).dropna().drop_duplicates()
#        pdCombined = pd.concat([basel, la, london]).replace('', np.nan).dropna().drop_duplicates()
        print("new line")
        return pdCombined
    #Save the combined files to the path specified
    def saveCleaned(self, dataframe):
        dataframe.to_csv('Resources\AQ cleaned.csv', index=False)

if __name__ == '__main__':
    a = UnifyAQ()
