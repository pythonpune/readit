import sqlite3
import sys

class DatabaseConnection(object):
    
    def __init__(self, cursor, db):
        
        """
        Create database connection.
        creates or opens file mydatabase with sqlite3 DataBase.
        get cursor object.
        create table.
        """
        
        try:
            self.db = sqlite3.connect('test.db')
           # db = sqlite3.connect(data/mydatabasie)
           
            self.cursor =  self.db.cursor()
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS bookmarks(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, url TEXT)
            ''')
            self.db.commit()

        except sqlite3.OperationalError:
            
            print("Table coulden't be created:")
    
    def add_url(self, url):
        """
        url will be adding to database.
        """
        self.url = url
         
        self.cursor.execute('''
        INSERT INTO bookmarks(url) VALUES (?)
        ''', (self.url,))
        self.db.commit()
       # self.db.close()
    
    def delete_url(self, urlid):
        """
        url can deleted as per id number provided.
        """
        self.urlid = urlid
        self.cursor.execute(''' DELETE FROM bookmarks WHERE id=? ''', (self.urlid,))
        self.db.commit()
        #self.db.close()
    
    def update_url(self, url):
        """
        url can be updated with respect to id.
        """

        self.url = url
        self.arr[2] = self.url
        urlid = arr[0]
        urlname = arr[1]
        self.cursor.execute(''' UPDATE bookmarks SET id=? WHERE url=?''',(urlid, urlname) )
        self.db.commit()
        #self.db.close()

    def show_url(self):
        """
        all urls from database shown to user on screen.
        """

        self.cursor.execute(''' SELECT id, url FROM bookmarks ''')
        all_row = self.cursor.fetchall()
        for row in all_row:
            print(row)
      #  print("data show succes")
        self.db.commit()
        #self.db.close()


    
