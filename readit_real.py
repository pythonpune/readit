import argparse
import psycopg2
import sys
import datetime
import os
import requests

class DatabaseConnection(object):

    def __init__(self, connection, cursor):
        try: 
            # database connection
            self.connection = psycopg2.connect(database="mydb" ,  user="testuser" , password="test", host="localhost" , port="5432")
             
            #print("open successfully")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            #print("connection successful")
        except:
            print("cannot connect to database")
    
    def create_table(self):
        # Created table to store urls
        create_table_command = "CREATE TABLE bookmarks(ID serial PRIMARY KEY, URL varchar(500), Date date not null default CURRENT_DATE)"
        self.cursor.execute(create_table_command)
        print("table created successfully")

    def insert_new_record(self, url):
        # data inserted into database table
        self.url = url
        insert_command = "INSERT INTO bookmarks(ID , URL , DATE) VALUES(DEFAULT, '"+ self.url +"' , DEFAULT)"
        print(insert_command)
        self.cursor.execute(insert_command)
        print("successfully inserted")
        
    def query_all(self):
        # Showing data added to table
        self.cursor.execute("SELECT * FROM bookmarks")
        rows = self.cursor.fetchall()
        print('-------'*10)
        print("%2s |  %15s|  %12s" % ('ID', 'DATE', 'URL'))
        print('-------'*10)
        for row in rows:
            print("%2s | %15s |  %12s" % (row[0], row[2], row[1]))

    def update_record(self, ID, URL):
        # Updating data of table
        update_command = "UPDATE bookmarks SET URL='"+URL+"' WHERE id="+str(ID)
        self.cursor.execute(update_command)
        print("successfully updated")

    def delete_record(self, num):
        # deletion of data from table
        self.num = str(num)
        
        delete_command = "DELETE FROM bookmarks WHERE bookmarks.id=" + self.num
        self.cursor.execute(delete_command)
        print("successful deletion")

    def drop_table(self):
        # drop table to remove all database of stored urls
        drop_table = "DROP TABLE bookmarks"
        self.cursor.execute(drop_table)
        print("table dropped")

if __name__== '__main__':


    database_connection = DatabaseConnection('','')
    # argparse use
    parser = argparse.ArgumentParser()
    parser.add_argument('default', nargs='*')
    parser.add_argument('-ct','-create',required=False,   help="create table to insert data" ,action="store_true")
    parser.add_argument('-dt','-drop',required=False,  help="drop table to delete all bookmarks" ,action="store_true")
    parser.add_argument('-a','-add', nargs='+', help="add url")
    parser.add_argument('-v','-view',required=False,help="view url",action="store_true")
    parser.add_argument('-u','-update', nargs=2, help="Update url by id")
    parser.add_argument('-d','-delete', help="delete url by id")
    parser.add_argument('-q', '-quiet', help="quiet", action="store_true")
    args = parser.parse_args()
   

    if args.a:
        # request used to check validation of urls
        x = len(args.a)
        i = 0
        while i < x:
            urldata = str(args.a[i])
            url = requests.get(urldata)
            if (404==url.status_code):
                print("Invalid URL...")
            else:
                database_connection.insert_new_record(args.a[i])
            i = i + 1
    
    elif args.v:

        database_connection.query_all()
    
    elif args.u:
    
        database_connection.update_record(args.u[0], args.u[1])
    
    elif args.d:

        database_connection.delete_record(args.delete)

    elif args.dt:

        database_connection.drop_table()

    elif args.ct:
        
        database_connection.create_table()

    elif args.q:

        database_connection.query_all()

    elif args.default:
        # url inserting in database
        j = 0
        y = len(args.defy)
        
        while j < y:
            urldata = str(args.defy[j])
            url = requests.get(urldata)
            if(404==url.status_code):
                print("invalid URL...")
            else:
                database_connection.insert_new_record(args.defy[j])
            j = j + 1
            

    else:

        print("-h, --help   show this help message and exit\n",args)
	
    


