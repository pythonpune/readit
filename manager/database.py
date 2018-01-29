import sqlite3
import datetime


class DatabaseConnection(object):

    def __init__(self, cursor, db):
        """
        Create database connection.
        creates or opens file mydatabase with sqlite3 DataBase.
        get cursor object.
        create table.
        """

        try:
            self.db = sqlite3.connect('test1.db')
            self.cursor = self.db.cursor()
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS bookmarks
            (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            url TEXT UNIQUE NOT NULL, date TEXT, time TEXT)''')
            self.db.commit()

        except sqlite3.OperationalError:

            print("Table coulden't be created:")

    def add_url(self, url):
        """
        url will be adding to database.
        """
        try:
            self.url = url
            date = datetime.date.today()
            start = datetime.datetime.now()
            time = start.strftime("%H:%M:%S")
            self.cursor.execute('''
            INSERT INTO bookmarks(url, date, time) VALUES (?, ?, ?)
            ''', (self.url, date, time))
            self.db.commit()
        except Exception as e1:
            print("URL is already present in database.", e1)

    def delete_url(self, urlid):
        """
        URLs can deleted as per id number provided.
        """
        try:
            self.urlid = urlid
            self.cursor.execute(
                ''' SELECT url FROM bookmarks where id=? ''', (self.urlid))
            rows = self.cursor.fetchone()
            for r in rows:
                print("Deleted url:--> ", r)
            self.cursor.execute(
                ''' DELETE FROM bookmarks WHERE id=? ''', (self.urlid,))
            self.db.commit()
        except Exception as e2:
            print("URL of this id is present not in database.", e2)

    def update_url(self, uid, url):
        """
        URLs can be updated with respect to id.
        """

        try:

            self.uid = uid
            self.url = url
            self.cursor.execute(
                ''' SELECT url FROM bookmarks WHERE id=?''', (self.uid))
            r = self.cursor.fetchone()
            for i in r:
                print("Replaced URL:--> ", i)
            self.cursor.execute(''' UPDATE bookmarks SET url=? WHERE id=?''',
                                (self.url, self.uid,))
            self.db.commit()
        except Exception as e3:
            print("Provided id is not present in database.", e3)

    def show_url(self):
        """
        All URLs from database displayed to user on screen.
        """
        try:
            self.cursor.execute(
                ''' SELECT id, url, date, time FROM bookmarks ''')
            all_row = self.cursor.fetchall()
            for row in all_row:
                print(row)
            self.db.commit()
        except Exception as e4:
            print("Databse is empty.", e4)

    def delete_all_url(self):
        """
        All URLs from database will be deleted.
        """
        try:
            self.cursor.execute(''' DELETE FROM bookmarks ''')
            self.db.commit()
        except Exception as e5:
            print("Database does not have any data.", e5)
