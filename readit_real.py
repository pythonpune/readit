import argparse
import psycopg2
import sys
import datetime
import os
import requests

class DatabaseConnection(object):

    def __init__(self, connection, cursor):
        try: 
            self.connection = psycopg2.connect(database="mydb" ,  user="testuser" , password="test", host="localhost" , port="5432")
             
            #print("open successfully")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            #print("connection successful")
        except:
            print("cannot connect to database")
    
    def create_table(self):
        create_table_command = "CREATE TABLE bookmarks(ID serial PRIMARY KEY, URL varchar(100), Date date not null default CURRENT_DATE)"
        self.cursor.execute(create_table_command)
        print("table created successfully")

    def insert_new_record(self, url):
        self.url = url
        insert_command = "INSERT INTO bookmarks(ID , URL , DATE) VALUES(DEFAULT, '"+ self.url +"' , DEFAULT)"
        print(insert_command)
        self.cursor.execute(insert_command)
        print("successfully inserted")
        
    def query_all(self):
        self.cursor.execute("SELECT * FROM bookmarks")
        cats = self.cursor.fetchall()
        for cat in cats:
            print("{0}".format(cat))

    def update_record(self):
        update_command = "UPDATE bookmarks SET URL='google.com' WHERE id=1"
        self.cursor.execute(update_command)
        print("successfully updated")

    def delete_record(self, num):
        self.num = int(num)
        print("selfnum:",self.num)
        delete_command = "DELETE FROM bookmarks WHERE id=?"
        self.cursor.execute(delete_command, num)
        print("successful deletion")

    def drop_table(self):
        drop_table = "DROP TABLE bookmarks"
        self.cursor.execute(drop_table)
        print("table dropped")

if __name__== '__main__':


    database_connection = DatabaseConnection('','')

    parser = argparse.ArgumentParser()
    parser.add_argument('-create','-ct',required=False,   help="create table to insert data" ,action="store_true")
    parser.add_argument('-drop','-dt',required=False,  help="drop table to delete all bookmarks" ,action="store_true")
    parser.add_argument('-add','-a',   help="add url")
    parser.add_argument('-view','-v',required=False,help="view url",action="store_true")
   
    parser.add_argument('-update','-u', help="Update url by it's id")
    parser.add_argument('-delete','-d', help="delete url by it's id")
    args = parser.parse_args()
    
    if args.add:
        url=str(args.data)
        urldata=requests.get(url)
        if(404==urldata.status_code):
                print("Invalid URL, please check Url..!!")
        else:
                database_connection.insert_new_record(args.add)
    
    elif args.view:
        database_connection.query_all()
    
    elif args.update:

        database_connection.update_record(args.update)
    
    elif args.delete:

        database_connection.delete_record(args.delete, num)

    elif args.drop:

        database_connection.drop_table()

    elif args.create:                                                                                                                                        database_connection.create_table()

    else:
	
        database_connection.insert_new_record(args.add)



