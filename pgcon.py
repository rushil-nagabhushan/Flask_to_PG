import psycopg2

con = psycopg2.connect(host="localhost",database="testdb",user="testing",password="testing")
cur = con.cursor()

class DBC:
    # default connection and cursor provided for my system and my test database
    def __init__(self, con=con, cur=cur):
        self.con = con
        self.cur = cur

    # simple function to create and structure the data
    def createTable(self):
        schema_cr = 'CREATE SCHEMA IF NOT EXISTS testscm;'
        self.cur.execute(schema_cr)
        table_cr = 'CREATE TABLE IF NOT EXISTS testscm.stats (name VARCHAR (50), matches integer, goals integer, assists integer);'
        self.cur.execute(table_cr)
        self.con.commit()
        msg = self.con.commit()
        return msg

    # simple function to display the database so far
    def displayDB(self):
        cur.execute("SELECT * FROM testscm.stats")
        rows = cur.fetchall()
        con.commit()
        return rows

    # simple function to INSERT values to database
    def addToDB(self, name: str, matches: int, goals: int, assists: int):
        name = "'" + name + "'"
        query = "INSERT INTO testscm.stats "
        values = 'VALUES (' + name + ',' + str(matches) + ',' + str(goals) + ',' + str(assists) + ')'
        conflict = ' ON CONFLICT ON CONSTRAINT stats_pkey DO UPDATE '
        update = ' SET name = ' + name + ', matches =  ' + str(matches) + ', goals = ' + str(goals) + ', assists = ' + str(assists) + ';'
        query_msg = query + values + conflict + update
        print(query_msg)
        self.cur.execute(query_msg)
        self.con.commit()
        
    # simple function to DELETE values from database
    def deleteFromDB(self, name: str):
        name = "'" + name + "'"
        query = "DELETE FROM testscm.stats WHERE name = " + name + ';'
        self.cur.execute(query)
        self.con.commit()
