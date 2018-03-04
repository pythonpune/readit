'''
 Copyright (C) 2017, 2018 projectreadit organization and contributors.
 This file is part of Readit - Command Line Bookmark Manager Tool.

 This project is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This project is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with readit.  If not, see <http://www.gnu.org/licenses/>.
'''

import sqlite3  # library of database used for project
import datetime  # used for getting current time and date
from beautifultable import BeautifulTable  # display output in table format
import webbrowser  # used to open url in browser
import os  # used to find home directory of user

date = datetime.date.today()

table = BeautifulTable()
table.left_border_char = '|'
table.right_border_char = '|'
table.top_border_char = '='
table.header_seperator_char = '='
table.column_headers = ["ID", "URL", "TAG", "DATE", "TIME"]


class DatabaseConnection(object):

    def __init__(self):
        """
        Calls the function init_db().
        """
        self.init_db("", "")

    def init_db(self, cursor, db):
        """
        Create database connection.
        creates or opens file mydatabase with sqlite3 DataBase.
        get cursor object.
        create table.
        """

        try:
            config_path = os.path.join(
                os.path.expanduser('~'), ".config/readit")
            if not os.path.exists(config_path):
                os.mkdir(config_path)
        except OSError:
            print('Error: Creating directory.' + config_path)

        databasefile = os.path.join(config_path, "bookmarks.db")
        try:
            self.db = sqlite3.connect(databasefile)
            self.cursor = self.db.cursor()
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS bookmarks
            (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            url TEXT UNIQUE NOT NULL, tags TEXT, date TEXT, time TEXT)''')
            self.db.commit()

        except sqlite3.OperationalError:

            print("Table coulden't be created:")

    def add_url(self, url):
        """
        URL will be adding to database.
        """

        try:
            self.url = url
            global date
            start = datetime.datetime.now()
            time = start.strftime("%H:%M:%S")
            self.cursor.execute('''
            INSERT INTO bookmarks(url, tags, date, time) VALUES (?, ?, ?, ?)
            ''', (self.url, "None", date, time))
            self.db.commit()
            print("Bookmarked.")
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
            start = datetime.datetime.now()
            time = start.strftime("%H:%M:%S")
            self.cursor.execute(
                '''INSERT INTO bookmarks(url, tags, date, time)
                VALUES(?, ?, ?, ?)''', (self.url, self.tag, date, time))
            self.db.commit()
            print("Bookmarked.")
        except Exception as t:
            print("Invalid input:--> ", t)

    def delete_url(self, url_id):
        """
        URLs can deleted as per id number provided.
        """
        try:
            self.url_id = url_id
            self.cursor.execute(
                ''' SELECT url FROM bookmarks where id=? ''', (self.url_id,))
            url_to_delete = self.cursor.fetchone()
            for deleted_url in url_to_delete:
                print("Deleted URL:--> ", deleted_url)
            self.cursor.execute(
                ''' DELETE FROM bookmarks WHERE id=? ''', (self.url_id,))
            self.db.commit()
        except Exception as e2:
            print("URL of this id is present not in database.", e2)

    def update_url(self, url_id, url):
        """
        URLs can be updated with respect to id.
        """

        try:

            self.url_id = url_id
            self.url = url
            self.cursor.execute(
                ''' SELECT url FROM bookmarks WHERE id=?''', (self.url_id,))
            url_to_replace = self.cursor.fetchone()
            for url_replaced in url_to_replace:
                print("Replaced URL:--> ", url_replaced)
            self.cursor.execute(''' UPDATE bookmarks SET url=? WHERE id=?''',
                                (self.url, self.url_id,))
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
            all_bookmarks = self.cursor.fetchall()
            if all_bookmarks == []:
                print("Database is empty.")
            else:
                for bookmark in all_bookmarks:
                    table.append_row(
                        [bookmark[0], bookmark[1], bookmark[2],
                         bookmark[3], bookmark[4]])
                print(table)
                self.db.commit()

        except Exception as e4:
            print("Database is empty.", e4)

    def search_by_tag(self, tag):
        """
        Group of URLs displayed with respect to Tag.
        """
        try:
            self.tag = tag
            self.cursor.execute(
                ''' SELECT id, url, tags, date, time
                                FROM bookmarks WHERE tags=?''', (self.tag,))
            all_bookmarks = self.cursor.fetchall()
            if all_bookmarks == []:
                print("Tag is not present in database.")
            else:
                for bookmark in all_bookmarks:
                    table.append_row(
                        [bookmark[0], bookmark[1], bookmark[2],
                         bookmark[3], bookmark[4]])
                print(table)
                self.db.commit()
        except Exception as t1:
            print("Specified Tag is invalid:--> ", t1)

    def delete_all_url(self):
        """
        All URLs from database will be deleted.
        """
        try:
            if self.check_url_db():
                print("Database is empty.")
            else:
                self.cursor.execute(''' DELETE FROM bookmarks ''')
                print("All bookmarks deleted.")
            self.db.commit()

        except Exception as e5:
            print("Database does not have any data:--> ", e5)

    def check_url_db(self):
        """
        Checks Whether URL is present in database or not.
        """
        self.cursor.execute(
            ''' SELECT id, url, tags, date, time FROM bookmarks ''')
        all_bookmarks = self.cursor.fetchall()
        if all_bookmarks == []:
            return True
        else:
            return False

    def open_url(self, urlid):
        """
        Opens the URL in default browser.
        """
        try:
            self.urlid = urlid
            self.cursor.execute(
                ''' SELECT url FROM bookmarks WHERE id=?''', (self.urlid,))
            all_row = self.cursor.fetchone()
            for url in all_row:
                webbrowser.open_new(url)
            self.db.commit()
        except Exception as i:
            print("Specified ID is invalid:--> ", i)
