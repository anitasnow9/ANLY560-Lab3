Main.java
import java.sql.*;
import java.util.ArrayList;

public class Main

    public static void main(String[] args)
        Person person = new Person(Barrack,Obama,      12, 5136112,12345);
        Person person1 = new Person(Name1, LastName6, 13, 5136113,12346);
        Person person2 = new Person(Name2, LastName7, 14, 5136114,12347);
        Person person3 = new Person(Name3, LastName8, 15, 5136115,12348);
        Person person4 = new Person(Name4, LastName9, 16, 5136116,12349);
        Person person5 = new Person(Name5, LastName10, 17, 5136117,12350);


        createTable();
        insertPerson(person);
        insertPerson(person1);
        insertPerson(person2);
        insertPerson(person3);
        insertPerson(person4);
        insertPerson(person5);

        System.out.println(selectPerson(4));
        for(Person p: findAllPeople())
            System.out.println(p);
       
        deletePerson(4);

        for(Person p: findAllPeople())
            System.out.println(p);
       

   

    public static Connection deletePerson(int id)
        Connection connection = null;
        Statement stmt = null;

        try
            connection = getConnection();
            connection.setAutoCommit(false);

            stmt = connection.createStatement();
            String sql = DELETE from MARK where ID= + id + ;;
            stmt.executeUpdate(sql);
            connection.commit();
            connection.close();

            System.out.println((Deleted Person + id + ) done successfully);
        catch ( Exception e )
            System.out.println(e);
            connection = null;
       
        return connection;


   

    public static ArrayList findAllPeople()
        Connection connection = null;
        Statement statement = null;
        ArrayList person = new ArrayList<>();

        try
            connection = getConnection();
            connection.setAutoCommit(false);

            statement = connection.createStatement();
