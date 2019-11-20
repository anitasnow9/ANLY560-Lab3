import MySQLdb

class DBConnection:
    def __init__(self, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME):
        self.host = DB_HOST
        self.port = DB_PORT
        self.user = DB_USER
        self.password = DB_PASSWORD
        self.name = DB_NAME
        self.conn = None
        
    def get_conn(self):
        self.conn = MySQLdb.connect(host = self.host,
                                    port = self.port,
                                    db = self.name,
                                    user = self.user,
                                    passwd = self.password)
    
    mydbconnobj = DBConnection('localhost',3306,'admin','adm123','sakila')
    mydbconn = mydbconnobj.get_conn()
 

class Actor
    def __init__(self, actor_id, first_name, last_name, last_update):
        self.actor_id = actor_id
        self.first_name = first_name
        self.last_name = last_name
        self.last_update = last_update

act_1 = Actor('1234567','Ning','Wang',NULL)
act_2 = Actor('7654321','User','Test',NULL)
    
add_actor = ("INSERT INTO actor "
             "(actor_id, first_name, last_name, last_update) "
             "VALUES (%s, %s, %s, %s)")
    
cursor.execute(add_actor, act_1)
cursor.execute(add_actor, act_2)

sql_command = """SELECT * FROM actor WHERE last_update = (SELECT MAX(last_update) FROM actor)"""
cursor.execute(sql_command)

cursor.close()
