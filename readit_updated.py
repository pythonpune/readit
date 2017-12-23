#!/usr/bin/env python
import os
import argparse
import sys
import psycopg2
import datetime

def main():
    parser = argparse.ArgumentParser(description="An easy to use cli to-do list program.")
    subparser = parser.add_subparsers(help="Commands you can use with the program", 
                                      dest='command')
    
    #subcommand add    
    parser_create = subparser.add_parser('add', 
                                        help="Add a new item to the list.")
    parser_create.add_argument('text', 
                                type=str, 
                                help="Enter the text to be added to the list.")
    parser_create.add_argument('-p',
                                type=str, 
                                choices=['h','m','l'],
                                default="None", 
                                help="Set priority for the item. Options: h=high, m=medium, l=low.")
    parser_create.add_argument('-d',
                                type=str,
                                default="None",
                                help="Set a deadline for the item. Format='2017-12-31'")

    #subcommand list
    parser_list = subparser.add_parser('list', 
                                        help="Show the contents of the list.")

    #subcommand remove
    parser_remove = subparser.add_parser('remove', 
                                        help="Remove an item from the list.")
    parser_remove.add_argument('no', 
                                type=int, 
                                help="Enter the no of the item you want to remove.")

    args = parser.parse_args()

    if args.command == 'add':
        add(args.text,args.p,args.d) 
    elif args.command == 'list':
        showlist()
    elif args.command == 'remove':
        remove(args.no)
    else:
        parser.print_help()


def add(add,deadline,priority):
	conn = psycopg2.connect(database="test", user = "postgres1", password = "postgres1", host = "localhost", port = "5432")
	print("Opened database successfully")
	cur = conn.cursor()
	data=str(add)
	#error showing here
	date1=str(deadline)
	lastdate=datetime.datetime.strptime( date1, '%Y-%m-%d')
	#Up to this
	prio=str(priority)
	cur.execute('''CREATE TABLE IF NOT EXISTS COMPANY(ID BIGSERIAL PRIMARY KEY,TAGNAME TEXT NOT NULL, DEADLINE date, PRIORITY CHAR(50);''')
	print("Table created successfully")
	cur.execute("INSERT INTO COMPANY (ID,TAGNAME,DEADLINE,PRIORITY) VALUES(data,lastdate,prio)");
	conn.commit()
	conn.close()
	showlist()

#display list
def showlist():
    conn = psycopg2.connect(database="test", user = "postgres1", password = "postgres1", host = "localhost", port = "5432")
    print("Opened database successfully")
    cur=conn.cursor()
    cur.execute("SELECT * from COMPANY")
    rows = cur.fetchall()
    for row in rows:
        print("ID = ",row[0])
        print("NAME = ",row[1])
        print("DEADLINE = ",row[2])
        print("PRIORITY = ",row[3], "\n")
        print("Operation done successfully")
        conn.close()

#Delete operation
def remove(num):
    num1=int(num)
    conn = psycopg2.connect(database="test", user = "postgres1", password = "postgres1", host = "localhost", port = "5432")
    print("Opened database successfully")
    cur = conn.cursor()
    cur.execute("DELETE from COMPANY where ID=num1;")
    conn.commit
    print("Total number of rows deleted :", cur.rowcount)
    showlist()


main() 

