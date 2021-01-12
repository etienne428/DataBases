
class pollutantDictionary:

    # Dictionary used in order to calculate ppb to µg/m^3. CO is already in ppm
    def __init(self):
        self.dict = {'SO2': 2.6647 ,'NO': 1.2741, 'NO2': 1.9123, 'CO': 1.1640*1000, 'O3': 1.9954}

