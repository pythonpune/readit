# Copyright (C) 2017, 2018 projectreadit organization and contributors.
# This file is part of Readit - Command Line Bookmark Manager Tool.
#
# This project is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This project is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with readit.  If not, see <http://www.gnu.org/licenses/>.


import sqlite3  # library of database used for project
import datetime  # used for getting current time and date
from beautifultable import BeautifulTable  # display output in table format
import webbrowser  # used to open url in browser
import os  # used to find home directory of user
import csv  # used to store bookmarks in CSV file
from glob import glob  # used to find path name
from os.path import expanduser  # used to perform operations on pathnames

date = datetime.date.today()

table = BeautifulTable()
table_tag = BeautifulTable()
table.left_border_char = '|'
table.right_border_char = '|'
table.top_border_char = '='
table.header_separator_char = '='
table.column_headers = ["ID", "URL", "TAG", "DATE", "TIME"]
table_tag.left_border_char = '|'
table_tag.right_border_char = '|'
table_tag.top_border_char = '='
table_tag.header_separator_char = '='
table_tag.column_headers = ["Available TAGs"]


class DatabaseConnection(object):
    """Class to perform database operations.
    """

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

        Attributes
        ----------
        db : sqlite database connection.
        cursor : sqlite database cursor.
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

            print("Table coulden't be created:-->")

    def add_url(self, url):
        """
        URL will be adding to database.


        Parameters
        ----------
        url : str
            A URL to add in database.

        Returns
        -------
        str
            A URL inserted in database.
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
            self.url_info(url)

    def tag_url(self, tag_name, tagged_url):
        """
        URLs can be added by respective Tags.

        Parameters
        ----------
        tag_name : str
            A comma separated tag to URL.

        tagged_url : str
            A URL to be tagged.

        Returns
        -------
        str
            A URL inserted with tag.
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
            self.url_info(tagged_url)

    def list_all_tags(self):
        """
        Shows list of all available Tags in database.

        Returns
        -------
        list
            It returns all available Tags associated with URLs in database.
        """
        tag_list = set()
        try:
            self.cursor.execute('''SELECT tags FROM bookmarks''')
            tags_in_db = self.cursor.fetchall()
            for tags_available in tags_in_db:
                tag_list.add(tags_available)
            tag_list = set(tag_list)
            tag_list = list(tag_list)
            tag_list.sort(reverse=False)
            for tag_in_list in tag_list:
                table_tag.append_row(tag_in_list)
            print(table_tag)
            self.db.commit()
        except Exception as tg:
            print("Tags are not found in database:-->", tg)

    def delete_url(self, url_id):
        """
        URLs can deleted as per id number provided.

        Parameters
        ----------
        urlid : int
            id of url present in database.

        Returns
        -------
        str
            A URL deleted from database.
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
            print("URL of this id is present not in database:-->", e2)

    def update_url(self, url_id, url):
        """
        URLs can be updated with respect to id.

        Parameters
        ----------
        url_id : int
            id of url which present in database.

        url : str
            A URL to update.

        Returns
        -------
        str
            A URL updated in database.
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

        Returns
        -------
        list
            A table representing all bookmarks.
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
            print("Database is empty:-->", e4)

    def search_by_tag(self, tag):
        """
        Group of URLs displayed with respect to Tag.

        Parameters
        ----------
        tag : str
            tag to search URLs.

        Returns
        -------
        list
            A table containing bookmarks.

        """
        try:
            self.tag = tag
            self.cursor.execute(
                ''' SELECT id, url, tags, date, time
                                FROM bookmarks WHERE tags=?''', (self.tag,))
            all_bookmarks = self.cursor.fetchall()
            if all_bookmarks == []:
                print("*" * 26, "\nThis TAG is not available.\n", "*" * 25)
                self.list_all_tags()
            else:
                for bookmark in all_bookmarks:
                    table.append_row(
                        [bookmark[0], bookmark[1], bookmark[2],
                         bookmark[3], bookmark[4]])
                print(table)
                self.db.commit()
        except Exception as t1:
            print("*" * 26, "\nThis TAG is not available.\n", "*" * 25)
            self.list_all_tags()

    def delete_all_url(self):
        """
        All URLs from database will be deleted.

        Returns
        -------
        null
            All URLs will be removed from database.
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

        Returns
        -------
        bool
            It returns TRUE if URL is present in database else False.
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

        Parameters
        ----------
        urlid:
            id of url present in database.

        Returns
        -------
        str
            A URL opened in default browser.
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

    def export_urls(self):
        """
        Exporting urls to csv file from database.

        Returns
        -------
        csv file
            A file containing exported bookmarks records.
        """
        try:
            config_path = os.path.expanduser("~/.config/readit")
            if not os.path.exists(config_path):
                print("File path does not exist: " + config_path)
        except OSError:
            print("Error: Finding directory: " + config_path)
        databasefile = os.path.join(config_path, "bookmarks.db")
        try:
            self.conn = sqlite3.connect(glob(expanduser(databasefile))[0])
            self.cursor = self.conn.cursor()
            self.cursor.execute("select * from bookmarks")
            with open("exported_bookmarks.csv", "w", newline='') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter='\t')
                csv_writer.writerow([i[0] for i in self.cursor.description])
                csv_writer.writerows(self.cursor)
                dirpath = os.getcwd()
                print(
                    "File containing exported bookmarks available at " +
                    dirpath +
                    "/exported_bookmarks.csv")
        except Exception as ex:
            print("Bookmarks are not exported in csv file-->" + ex)

    def url_info(self, url):
        """
        Display the information regarding already present URL in database.

        Parameters
        ----------
        url : str
            url to search it's information from database.

        Returns
        -------
        str
            All the information about particular URL.
        """
        try:
            self.url_exist = url
            self.cursor.execute(
                ''' SELECT id, url, tags, date, time
                            FROM bookmarks WHERE url=?''', (self.url_exist,))
            all_bookmarks = self.cursor.fetchall()
            print("*" * 31, "\nThis URL is already bookmarked.\n", "*" * 30)
            for bookmark in all_bookmarks:
                table.append_row(
                    [bookmark[0], bookmark[1], bookmark[2],
                        bookmark[3], bookmark[4]])
            print(table)
            self.db.commit()
        except Exception as t2:
            print("Specified URL is invalid:--> ", t2)
