import pandas as pd

path = 'Resources\links.csv'
path2 = 'Resources\detectors_public.csv'

"""
This class is used in order to clean the links from the eth database.
We want to get the Detector IDs into the Link table.
"""
class LinkClean:

    def __init__(self):
        self.dflink = pd.read_csv(path)
        self.detector = pd.read_csv(path2)

    #By joining on linkID we get the Detector ID as attribute in links
    def join(self):
        return pd.merge(self.dflink, self.detector, on="linkid")

if __name__ == '__main__':
    a = LinkClean()
    x = a.join()
    x[['detid','long_x', 'lat_x', 'order', 'piece', 'linkid', 'group', 'citycode_x'
       ]].to_csv('Resources\linksCleaned.csv', index=False)

