import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnectionJava {
	private static final String URL = "jdbc:mysql://localhost:3306/your_database_name";
	private static final String USER = "LocalHost";
	private static final String PASSWORD = "Anjali2004";
	public static Connection getConnection() {
		Connection connection	= null;
			try {
				//	Load	the	MySQL	JDBC	driver
				Class.forName("com.mysql.cj.jdbc.Driver");
				//	Establish	the	connection
				connection	= DriverManager.getConnection(URL, USER, PASSWORD);
				System.out.println("Connected	to	MySQL	database!");
				} catch (ClassNotFoundException | SQLException e) {
					System.err.println("Connection	error:	" + e.getMessage());
								}
								return connection;
				}
				//	Optional:	Test	the	connection
}
