
#    Modules imported:

# psycopg2 module --- This is postgresql database module.
# sys module      --- This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
# os module 	--- This module helps to access environmental variable.
# datetime module	--- This module helps to get current date from system.
# requests module --- This module helps to check whether url is valid or not



import psycopg2
import sys
import datetime
import os
import requests

class DatabaseConnection(object):
    def __init__(self, connection, cursor):
    
        """
        This is initialised function. 
        Which creates connection to database.

        """	
        try: 
            # database connection

            self.connection = psycopg2.connect(database="mydb" ,  user="testuser" , password="test", host="localhost" , port="5432")
             
      
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            
        except:
            print("cannot connect to database")
    
        create_table_command = "CREATE TABLE IF NOT EXISTS bookmarks(ID serial PRIMARY KEY, URL varchar(500), Date date not null default CURRENT_DATE)"
        self.cursor.execute(create_table_command)

    def insert_new_record(self, url):
        """
	This function inserts the new records in databse table.

	"""
        self.url = url
        insert_command = "INSERT INTO bookmarks(ID , URL , DATE) VALUES(DEFAULT, '"+ self.url +"' , DEFAULT)"
        print(insert_command)
        self.cursor.execute(insert_command)
        print("successfully inserted")
        
    def query_all(self):
        """
	This function shows all databse.

	"""
        self.cursor.execute("SELECT * FROM bookmarks")
        rows = self.cursor.fetchall()
        print('-------'*10)
        print("%2s |  %15s|  %12s" % ('ID', 'DATE', 'URL'))
        print('-------'*10)
        for row in rows:
            print("%2s | %15s |  %12s" % (row[0], row[2], row[1]))

    def update_record(self, ID, URL):
        """
	This function updates the record with respect to IDs.

	"""
        update_command = "UPDATE bookmarks SET URL='"+URL+"' WHERE id="+str(ID)
        self.cursor.execute(update_command)
        print("successfully updated")

    def delete_record(self, num):
        """
	This function delete the records with respect to IDs.

	"""
        self.num = str(num)
        
        delete_command = "DELETE FROM bookmarks WHERE bookmarks.id=" + self.num
        self.cursor.execute(delete_command)
        print("successful deletion")

    def drop_table(self):
        """
	This function will delete all records 
        by droping table from database.

	"""
        drop_table = "DROP TABLE bookmarks"
        self.cursor.execute(drop_table)
        print("table dropped")

