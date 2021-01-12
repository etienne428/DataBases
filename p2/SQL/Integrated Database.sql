CREATE DATABASE integration;


CREATE TABLE Weather(
    Location         VARCHAR(15) NOT NULL,
    Date             VARCHAR(15)        NOT NULL,
    Time             VARCHAR(4)         NOT NULL,
    Temperature      FLOAT,
    WindSpeed        FLOAT,
    Precipitation    FLOAT,
    RelativeHumidity FLOAT,
    WindDirection    FLOAT,
    AirPressure      FLOAT,
    CloudCoverage    FLOAT,
    FOREIGN KEY (Location) REFERENCES Location (CityName),
    PRIMARY KEY (Location, Date, Time)
);


CREATE TABLE Location(
    CityName          VARCHAR(15) NOT NULL,
    PopulationDensity FLOAT,
    Population        INT,
    PRIMARY KEY (CityName)
);


CREATE TABLE AirPollution(
    Location VARCHAR(15) NOT NULL,
    Date VARCHAR(12) NOT NULL,
    Time VARCHAR(4) NOT NULL,
    SiteCode VARCHAR(15) NOT NULL,
    Species VARCHAR(20) NOT NULL,
    Value FLOAT,
    Longitude FLOAT,
    Latitude FLOAT,
    PRIMARY KEY (Date, Time, SiteCode, Species),
    FOREIGN KEY (Location) REFERENCES Location(CityName)
);

CREATE TABLE UTD(
    Date VARCHAR(15) NOT NULL,
    IntV INT NOT NULL,
    DetID VARCHAR(15) NOT NULL,
    Flow INT,
    Occupancy INT,
    Error INT,
    Location VARCHAR(20) NOT NULL,
    Speed INT,
    Time VARCHAR(4) NOT NULL,
    PRIMARY KEY (Date, DetID, Time),
    FOREIGN KEY (DetID) REFERENCES Detectors(DetID),
    FOREIGN KEY (Location) REFERENCES Location(CityName)
);

CREATE TABLE MVI(
    Location VARCHAR(12) NOT NULL,
    SiteCode INT NOT NULL,
    SiteName VARCHAR(50) NOT NULL,
    Direction VARCHAR(50) NOT NULL,
    LaneCode INT NOT NULL,
    LaneName VARCHAR(50),
    Date VARCHAR(10) NOT NULL,
    Time VARCHAR(4) NOT NULL,
    TrafficType VARCHAR(6),
    Total INT,
    MR INT,
    PW INT,
    PWPlus INT,
    Lief INT,
    LW INT,
    Sattelzug INT,
    Bus INT,
    andere INT,
    PRIMARY KEY(SiteCode, SiteName, Direction, Date, Time, Location, LaneCode),
    FOREIGN KEY(Location) REFERENCES Location(CityName)
);


CREATE TABLE Detectors(
    DetID VARCHAR(15) NOT NULL,
    length FLOAT,
    position FLOAT,
    fclass VARCHAR(15),
    road VARCHAR(15),
    lim INT,
    cityCode VARCHAR(20) NOT NULL,
    Lanes INT,
    LinkID INT,
    Longitude FLOAT,
    Latitude FLOAT,
    FOREIGN KEY (cityCode) REFERENCES Location(CityName),
    PRIMARY KEY (DetID)
);

CREATE TABLE Links(
    DetID VARCHAR(20) NOT NULL,
    Longitude FLOAT,
    Latitude FLOAT,
    Ordr INT NOT NULL,
    Piece INT,
    LinkID INT NOT NULL,
    Grou FLOAT,
    CityCode VARCHAR(20) NOT NULL,
    PRIMARY KEY(LinkID, DetID, Ordr),
    FOREIGN KEY(CityCode) REFERENCES Location(CityName),
    FOREIGN KEY(DetID) REFERENCES Detectors(DetID)
);



