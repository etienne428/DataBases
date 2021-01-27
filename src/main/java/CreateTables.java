public enum CreateTables {
    locationTable("CREATE TABLE Location(\n" +
            "    CityName          VARCHAR(15) NOT NULL,\n" +
            "    PopulationDensity FLOAT,\n" +
            "    Population        INT,\n" +
            "    PRIMARY KEY (CityName)\n" +
            ");"),
    weatherTable("CREATE TABLE Weather " +
            "(Location         VARCHAR(15)   NOT NULL," +
            " Date             VARCHAR(15)   NOT NULL," +
            " Time             VARCHAR(4)    NOT NULL," +
            " Temperature      FLOAT," +
            " WindSpeed        FLOAT," +
            " Precipitation    FLOAT," +
            " RelativeHumidity FLOAT," +
            " WindDirection    FLOAT," +
            " AirPressure      FLOAT," +
            " CloudCoverage    FLOAT," +
            " FOREIGN KEY (Location) REFERENCES Location (CityName)," +
            " PRIMARY KEY (Location, Date, Time))"),
    airPollutionTable("CREATE TABLE AirPollution(\n" +
            "    Location VARCHAR(15) NOT NULL,\n" +
            "    Date VARCHAR(12) NOT NULL,\n" +
            "    Time VARCHAR(4) NOT NULL,\n" +
            "    SiteCode VARCHAR(15) NOT NULL,\n" +
            "    Species VARCHAR(20) NOT NULL,\n" +
            "    Value FLOAT,\n" +
            "    Longitude FLOAT,\n" +
            "    Latitude FLOAT,\n" +
            "    PRIMARY KEY (Date, Time, SiteCode, Species),\n" +
            "    FOREIGN KEY (Location) REFERENCES Location(CityName)\n" +
            ");"),
    detectorsTable("CREATE TABLE Detectors(\n" +
            "    DetID VARCHAR(15) NOT NULL,\n" +
            "    length FLOAT,\n" +
            "    position FLOAT,\n" +
            "    fclass VARCHAR(15),\n" +
            "    road VARCHAR(15),\n" +
            "    lim INT,\n" +
            "    cityCode VARCHAR(20) NOT NULL,\n" +
            "    Lanes INT,\n" +
            "    LinkID INT,\n" +
            "    Longitude FLOAT,\n" +
            "    Latitude FLOAT,\n" +
            "    FOREIGN KEY (cityCode) REFERENCES Location(CityName),\n" +
            "    PRIMARY KEY (DetID)\n" +
            ");"),
    UTDTable("CREATE TABLE UTD(\n" +
            "    Date VARCHAR(15) NOT NULL,\n" +
            "    IntV INT NOT NULL,\n" +
            "    DetID VARCHAR(15) NOT NULL,\n" +
            "    Flow INT,\n" +
            "    Occupancy INT,\n" +
            "    Error INT,\n" +
            "    Location VARCHAR(20) NOT NULL,\n" +
            "    Speed INT,\n" +
            "    Time VARCHAR(4) NOT NULL,\n" +
            "    PRIMARY KEY (Date, DetID, Time),\n" +
            "    FOREIGN KEY (DetID) REFERENCES Detectors(DetID),\n" +
            "    FOREIGN KEY (Location) REFERENCES Location(CityName)\n" +
            ");"),
    MVITable("CREATE TABLE MVI(\n" +
            "    Location VARCHAR(12) NOT NULL,\n" +
            "    SiteCode INT NOT NULL,\n" +
            "    SiteName VARCHAR(50) NOT NULL,\n" +
            "    Direction VARCHAR(50) NOT NULL,\n" +
            "    LaneCode INT NOT NULL,\n" +
            "    LaneName VARCHAR(50),\n" +
            "    Date VARCHAR(10) NOT NULL,\n" +
            "    Time VARCHAR(4) NOT NULL,\n" +
            "    TrafficType VARCHAR(6),\n" +
            "    Total INT,\n" +
            "    MR INT,\n" +
            "    PW INT,\n" +
            "    PWPlus INT,\n" +
            "    Lief INT,\n" +
            "    LW INT,\n" +
            "    Sattelzug INT,\n" +
            "    Bus INT,\n" +
            "    andere INT,\n" +
            "    PRIMARY KEY(SiteCode, SiteName, Direction, Date, Time, Location, LaneCode),\n" +
            "    FOREIGN KEY(Location) REFERENCES Location(CityName)\n" +
            ");"),
    linksTable("CREATE TABLE Links(\n" +
            "    DetID VARCHAR(20) NOT NULL,\n" +
            "    Longitude FLOAT,\n" +
            "    Latitude FLOAT,\n" +
            "    Ordr INT NOT NULL,\n" +
            "    Piece INT,\n" +
            "    LinkID INT NOT NULL,\n" +
            "    Grou FLOAT,\n" +
            "    CityCode VARCHAR(20) NOT NULL,\n" +
            "    PRIMARY KEY(LinkID, DetID, Ordr),\n" +
            "    FOREIGN KEY(CityCode) REFERENCES Location(CityName),\n" +
            "    FOREIGN KEY(DetID) REFERENCES Detectors(DetID)\n" +
            ");");
    String table;
    CreateTables(String s) {
        table = s;
    }

    public String getTable() {
        return table;
    }
}