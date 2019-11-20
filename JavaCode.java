import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class JDBC {
  private static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
  private static final String DB_URL = "jdbc:mysql://localhost/sakila";
  private static final String user = "admin";
  private static final String password = "adm123";
  
  public static void main(String[] args) {
    Connection conn = null;
    Statement stmt = null;
    try{
      Class.forName("com.mysql.jdbc.Driver");
      System.out.println("Connecting to database...");
      conn = DriverManager.getConnection(DB_URL,user,password);
      
      System.out.println("Creating statement...");
      stmt = conn.createStatement();
      String sql;
      sql = "SELECT actor_id, first_name, last_name FROM actor";
      ResultSet rs = stmt.executeQuery(sql);
      
      while(rs.next()){
        int actor_id = rs.getInt("actor_id");
        String firstname = rs.getString("first_name");
        String lastname = rs.getString("last_name");
        
        System.out.print("ActorID:" + actor_id);
        System.out.print(", First Name:" + first_name);
        System.out.print(", Last Name:" + last_name);
      }
    } catch(SQLException se){
      se.printStackTrace();
    }catch(Exception e){
      e.printStackTrace();
    } finally {
      try {
        if(conn!=null)
          con.close();
      } catch(SQLException se) {
      se.printStackTrace();
      }
      try {
        if(stmt!=null)
          stmt.close();
      } catch(SQLException se) {/*can't do anything */}
    }
    System.out.println("End");
  }
}


    
