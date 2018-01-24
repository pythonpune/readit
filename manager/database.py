import sqlite3


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
            (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, url TEXT)
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

    def delete_url(self, urlid):
        """
        url can deleted as per id number provided.
        """
        self.urlid = urlid
        self.cursor.execute(
            ''' DELETE FROM bookmarks WHERE id=? ''', (self.urlid,))
        self.db.commit()

    def update_url(self, uid, url):
        """
        url can be updated with respect to id.
        """
        self.uid = uid
        self.url = url
        self.cursor.execute(
            ''' UPDATE bookmarks SET url=? WHERE id=?''', (self.url, self.uid,))
        self.db.commit()

    def show_url(self):
        """
        all urls from database shown to user on screen.
        """

        self.cursor.execute(''' SELECT id, url FROM bookmarks ''')
        all_row = self.cursor.fetchall()
        for row in all_row:
            print(row)
        self.db.commit()
