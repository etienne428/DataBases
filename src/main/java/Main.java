import java.sql.*;

public class Main {

    private Connection con;

    public void addTables() throws SQLException {
        String insertTable = "LOAD DATA INFILE ?" +
                "INTO TABLE ?" +
                "FIELDS TERMINATED BY ','" +
                "LINES TERMINATED BY '\n'" +
                "IGNORE 1 LINES ;";

        PreparedStatement statement = con.prepareStatement(insertTable);
        // City name, population and density (inhabitant / m^2)
        // Source : https://www.ukpopulation.org/london-population/
//        statement.executeUpdate("INSERT INTO Location " + "VALUES ('London', 9021600, 5590)");
        // Source : http://www.usa.com/los-angeles-ca-population-and-races.htm
//        statement.executeUpdate("INSERT INTO Location " + "VALUES ('Los Angeles', 3862210, 2966)");
        // Source : https://www.statistik.bs.ch/haeufig-gefragt/einwohner/einwohnerzahl.html ,
        // https://www.statistik.bs.ch/haeufig-gefragt/basel-kompakt.html
//        statement.executeUpdate("INSERT INTO Location " + "VALUES ('Basel', 200407, 5574)");


        String[] CSVFile = {"Detectors.csv", "LinksCleaned.csv", "ETHTrafficCleaned.csv", "MVIcleaned.csv", "AQ_cleaned.csv"};//, "Weather_cleaned.csv"};
        String[] tableName = {"Detectors", "Links", "UTD", "MVI", "AirPollution"};//, "Weather"};

        for (int i = 0; i < 1/*CSVFile.length*/; i++) {
            statement.setString(1, "Resources\\" + CSVFile[i]);
            statement.setString(2, tableName[i]);
            statement.addBatch();
        }
        statement.executeBatch();
        statement.close();
    }

    private void createTables() throws SQLException {
        PreparedStatement statement = null;
        for (CreateTables table : CreateTables.values()) {
            System.out.println(table.getTable());
            statement = con.prepareStatement(table.getTable());
            statement.execute();
        }
        assert statement != null;
        statement.close();
    }

    private void start() {
        String password = "JEtadore_428";
        String userName = "etienne428";
        String url = "jdbc:mysql://localhost:3306/project?useSSL=false";
        try {
            con = DriverManager.getConnection(url, userName, password);
            System.out.println("Connecting to Database...");
//            createTables();
            addTables();
            con.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        Main main = new Main();
        main.start();
    }
}