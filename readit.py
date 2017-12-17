import argparse
import psycopg2
import sys
import datetime
import os

def add_url(add):
    print("add function:"+add)
    conn = psycopg2.connect(database= "mydb", user = "testuser", password = "test", host = "localhost", port = "5432")
    print("Opened database successfully")
    cur = conn.cursor()
    data=str(add)
   # lastdate=datetime.datetime.strptime( date1, '%Y-%m-%d')

    cur.execute('''CREATE TABLE IF NOT EXISTS COMPANY4(id SERIAL PRIMARY KEY, lastdate  date not null default CURRENT_DATE, URL VARCHAR(100))''');
    print("Table created successfully")
    cur.execute("INSERT INTO COMPANY4(id, lastdate, URL) VALUES(DEFAULT, DEFAULT,'"+ data+"')")
    conn.commit()
    print("data inserted")

    conn.close()
    print("data inserted")
    view_url()


def view_url():
    conn = psycopg2.connect(database="mydb", user = "testuser", password = "test", host = "localhost", port = "5432")
    print("Opened database successfully")
    cur=conn.cursor()
    cur.execute("SELECT * from COMPANY4")
    rows = cur.fetchall()
    for row in rows:
        print("ID = ",row[0])
        print("lastdate = ",row[1])
        print("url = ",row[2])
  #      print("Operation done successfully")
        conn.close()


def modify_url(modify):
    print("Modify function:"+modify)

def delete_url(num):
  #  print("delete url:"+delete)
    num1=int(num)
    conn = psycopg2.connect(database="mydb", user = "testuser", password = "test", host = "localhost", port = "5432")
    print("Opened database successfully")
    cur = conn.cursor()
    cur.execute("DELETE FROM COMPANY4 WHERE id = %s",(num1,))
    conn.commit 
    print("Total number of rows deleted :", cur.rowcount)
   # view_url()

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-add','-a',   help="add url")
    parser.add_argument('-view','-v',required=False,help="view url",action="store_true")
   # parser.add_argument('',required=True,help="view url",action="store_true")
    parser.add_argument('-modify','-m', help="modify url")
    parser.add_argument('-delete','-d', help="delete url")
    args = parser.parse_args()
    
    if args.add: 
        add_url(args.add)
    
    elif args.view:
        view_url()
    
    elif args.modify:
        modify_url(args.modify)
    
    elif args.delete:
        delete_url(args.delete)
    else:
        add_url(args.add)

if __name__ == '__main__':
    Main()
