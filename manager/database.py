import sqlite3
import datetime

date = datetime.date.today()
start = datetime.datetime.now()
time = start.strftime("%H:%M:%S")


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
            self.cursor = self.db.cursor()
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS bookmarks
            (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            url TEXT UNIQUE NOT NULL, tags TEXT, date TEXT, time TEXT)''')
            self.db.commit()

        except sqlite3.OperationalError:

            print("Table coulden't be created:")

    def add_url(self, url):
        """
        url will be adding to database.
        """

        try:
            self.url = url
            global date
            global time
            self.cursor.execute('''
            INSERT INTO bookmarks(url, tags, date, time) VALUES (?, ?, ?, ?)
            ''', (self.url, None, date, time))
            self.db.commit()
        except Exception as e1:
            print("URL is already present in database.", e1)

    def tag_url(self, tag_name, tagged_url):
        """
        URLs can be added by respective Tags.
        """
        self.tag = tag_name
        self.url = tagged_url
        try:
            global date
            global time
            self.cursor.execute(
                '''INSERT INTO bookmarks(url, tags, date, time)
                VALUES(?, ?, ?, ?)''', (self.url, self.tag, date, time))
            self.db.commit()
        except Exception as t:
            print("Exception Caught:--> ", t)

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
            print("Provided id is not present or URL is already in database")
            print(":--> ", e3)

    def show_url(self):
        """
        All URLs from database displayed to user on screen.
        """
        try:
            self.cursor.execute(
                ''' SELECT id, url, tags, date, time FROM bookmarks ''')
            all_row = self.cursor.fetchall()
            print("ID | URL | TAG | DATE | TIME")
            for row in all_row:
                print('{0} | {1} | {2} | {3} | {4}'.format(
                    row[0], row[1], row[2], row[3], row[4]))
            self.db.commit()
        except Exception as e4:
            print("Databse is empty.", e4)

    def search_by_tag(self, tag):
        """
        Group of URLs displayed with respect to Tag.
        """
        try:
            self.tags = tag
            self.cursor.execute(
                ''' SELECT id, url, tags, date, time
                                FROM bookmarks WHERE tags=?''', (self.tags,))
            all_row = self.cursor.fetchall()
            print("ID | URL | TAG | DATE | TIME")
            for row in all_row:
                print('{0} | {1} | {2} | {3} | {4}'.format(
                    row[0], row[1], row[2], row[3], row[4]))
            self.db.commit()
        except Exception as t1:
            print("Specified Tag is invalid:--> ", t1)

    def delete_all_url(self):
        """
        All URLs from database will be deleted.
        """
        try:
            self.cursor.execute(''' DELETE FROM bookmarks ''')
            self.db.commit()
        except Exception as e5:
            print("Database does not have any data:--> ", e5)
