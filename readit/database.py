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
import csv
import datetime
import os
import sqlite3
import sys
import webbrowser
from glob import glob

date = datetime.date.today()


class DatabaseConnection(object):
    """Class to perform database operations."""

    def __init__(self):
        """
        Calls the function init_db().
        """
        self.config_path = os.path.expanduser("~/.config/readit")
        self.databasefile = os.path.join(self.config_path, "bookmarks.db")
        self._check_conf_dir()
        self.db = sqlite3.connect(self.databasefile)
        self.cursor = self.db.cursor()
        self.init_db()

    def _check_conf_dir(self):
        if not os.path.exists(self.config_path):
            os.mkdir(self.config_path)
            return True
        elif os.path.exists(self.config_path):
            return True
        return False

    def init_db(self):
        """Create database connection.
        creates or opens file mydatabase with sqlite3 Database.
        get cursor object.
        create table.
        """

        try:
            if self._check_conf_dir():
                self.cursor.execute(
                    """CREATE TABLE IF NOT EXISTS bookmarks
                    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    url TEXT UNIQUE NOT NULL, tags TEXT, date TEXT, time TEXT)"""
                )
                self.db.commit()
            else:
                raise IOError("Directory does not exists")

        except sqlite3.OperationalError as e:
            print("ERROR: Failed to create table.")
            print(e)
            sys.exit(1)

    def add_url(self, url):
        """
        URL will be adding to database.
        """

        try:
            self.url = url
            global date
            start = datetime.datetime.now()
            time = start.strftime("%H:%M:%S")
            self.cursor.execute(
                """
                INSERT INTO bookmarks(url, tags, date, time) VALUES (?, ?, ?, ?)
                """,
                (self.url, "None", date, time),
            )
            self.db.commit()
            return True
        except Exception:
            raise sqlite3.OperationalError

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
                """INSERT INTO bookmarks(url, tags, date, time)
                VALUES(?, ?, ?, ?)""",
                (self.url, self.tag, date, time),
            )
            self.db.commit()
            return True
        except Exception:
            raise sqlite3.OperationalError

    def list_all_tags(self):
        """
        Shows list of all available Tags in database.
        """
        tag_list = set()
        try:
            self.cursor.execute("""SELECT tags FROM bookmarks""")
            tags_in_db = self.cursor.fetchall()
            for tags_available in tags_in_db:
                tag_list.add(tags_available)
            tag_list = set(tag_list)
            tag_list = list(tag_list)
            tag_list.sort(reverse=False)
            self.db.commit()
            return tag_list
        except Exception:
            raise sqlite3.OperationalError

    def delete_url(self, url_id):
        """
        URLs can deleted as per id number provided.
        """
        try:
            self.url_id = url_id
            self.cursor.execute(""" SELECT url FROM bookmarks where id=? """, (self.url_id,))
            deleted_url = self.cursor.fetchone()
            self.cursor.execute(""" DELETE FROM bookmarks WHERE id=? """, (self.url_id,))
            self.db.commit()
            if deleted_url:
                return True
            else:
                return False
        except Exception:
            raise sqlite3.OperationalError

    def update_url(self, url_id, url):
        """
        URLs can be updated with respect to id.
        """

        try:
            self.url_id = url_id
            self.url = url
            # To check whether URL is present in DB
            self.cursor.execute(""" SELECT url FROM bookmarks WHERE id=?""", (self.url_id,))
            self.cursor.execute(
                """ UPDATE bookmarks SET url=? WHERE id=?""", (self.url, self.url_id)
            )
            self.db.commit()
            return True
        except Exception:
            raise sqlite3.OperationalError

    def show_url(self):
        """
        All URLs from database displayed to user on screen.
        """
        try:
            self.cursor.execute(""" SELECT id, url, tags, date, time FROM bookmarks """)
            all_bookmarks = self.cursor.fetchall()
            self.db.commit()
            if all_bookmarks == []:
                return None
            else:
                return all_bookmarks
        except Exception:
            raise sqlite3.OperationalError

    def search_url(self, search_value):
        """
        Group of URLs displayed with respect to search_value.

        """
        try:
            self.search = search_value
            all_bookmarks = []
            if self.check_tag(search_value):
                self.cursor.execute(
                    """ SELECT id, url, tags, date, time
                                    FROM bookmarks WHERE tags=?""",
                    (self.search,),
                )
                all_bookmarks = self.cursor.fetchall()
            else:
                self.cursor.execute(""" SELECT * FROM bookmarks""")
                bookmarks = self.cursor.fetchall()
                for bookmark in bookmarks:
                    if search_value.lower() in bookmark[1]:
                        all_bookmarks.append(bookmark)
            self.db.commit
            if all_bookmarks == []:
                return None
            else:
                return all_bookmarks
        except Exception:
            raise sqlite3.OperationalError

    def delete_all_url(self):
        """
        All URLs from database will be deleted.
        """
        try:
            self.cursor.execute(""" DELETE FROM bookmarks """)
            self.db.commit()
            return True
        except Exception:
            raise sqlite3.OperationalError

    def open_url(self, url_id_tag):
        """
        Opens the URLs in default browser.
        """
        try:
            # TODO: Comnine these two lists of urls
            all_row = []
            all_row = self.check_id(url_id_tag)
            all_row.append(self.search_url(url_id_tag))
            if all_row:
                for bookmark in all_row:
                    webbrowser.open(bookmark[1])
                self.db.commit()
                return True
            else:
                print("Provide either valid url id or url tag name or any valid substring.")

            if all_row:
                for i in range(len(all_row)):
                    for url in all_row[i]:
                        webbrowser.open_new_tab(url)
                self.db.commit()
                return True
        except Exception:
            raise sqlite3.OperationalError

    def check_tag(self, url_tag):
        """
        Checks this tag is available in database.
        """
        try:
            self.cursor.execute(""" SELECT url FROM bookmarks WHERE tags=?""", (url_tag,))
            all_row = self.cursor.fetchall()
            self.db.commit()
            if all_row == []:
                return None
            return all_row
        except Exception:
            raise sqlite3.OperationalError

    def check_id(self, url_id):
        """
        Check this is available in database.
        """
        try:
            self.cursor.execute(""" SELECT url FROM bookmarks WHERE id=?""", (url_id,))
            all_row = self.cursor.fetchall()
            if all_row == []:
                return None
            return all_row
        except Exception:
            raise sqlite3.OperationalError

    def export_urls(self):
        """
        Exporting urls to csv file from database.
        """
        try:
            config_path = os.path.expanduser("~/.config/readit")
            if not os.path.exists(config_path):
                msg = "File path does not exist: " + config_path
                return False, msg
        except OSError:
            msg = "Error: Finding directory: " + config_path
            return False, msg
        databasefile = os.path.join(config_path, "bookmarks.db")
        try:
            self.conn = sqlite3.connect(glob(os.path.expanduser(databasefile))[0])
            self.cursor = self.conn.cursor()
            self.cursor.execute("select * from bookmarks")
            with open("exported_bookmarks.csv", "w", newline="") as csv_file:
                csv_writer = csv.writer(csv_file, delimiter="\t")
                csv_writer.writerow([i[0] for i in self.cursor.description])
                csv_writer.writerows(self.cursor)
                dirpath = os.getcwd() + "/exported_bookmarks.csv"
                return dirpath
        except Exception:
            raise sqlite3.OperationalError

    def url_info(self, url):
        """
        Display the information regarding already present URL in database.
        """
        try:
            self.url_exist = url
            self.cursor.execute(
                """ SELECT id, url, tags, date, time FROM bookmarks WHERE url=?
                """,
                (self.url_exist,),
            )
            all_bookmarks = self.cursor.fetchall()
            self.db.commit()
            return all_bookmarks
        except Exception:
            raise sqlite3.OperationalError
