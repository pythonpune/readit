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
import tkinter as tk
import webbrowser
from glob import glob
from tkinter import filedialog

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
                raise IOError("\nDirectory does not exists")
        except sqlite3.OperationalError as e:
            print("\nERROR: Failed to create table in the database.")
            print(f"\nSQLite Error: {str(e)}")
            sys.exit(1)
        
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            sys.exit(1)

    def add_url(self, url):
        """
        Add a URL to the database. 
        If the URL already exists, provide a user-friendly error message.
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
        
        except sqlite3.IntegrityError as e:
            if 'UNIQUE constraint failed' in str(e):
                print(f"\nError: The URL '{self.url}' already exists in the database.")
                return False
            else:
                print(f"\nDatabase error: {str(e)}")
                return False

        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            return False

    def tag_url(self, tag_name, tagged_url):
        """
        URLs can be added by respective Tags. 
        If the URL already exists, provide a user-friendly error message.
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
        
        except sqlite3.IntegrityError as e:
            if 'UNIQUE constraint failed' in str(e):
                print(f"\nError: The URL '{self.url}' has already been tagged.")
                return False
            else:
                print(f"\nDatabase error: {str(e)}")
                return False

        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            return False

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
            # Check if the URL exists before attempting to delete
            self.cursor.execute(""" SELECT url FROM bookmarks WHERE id=? """, (self.url_id,))
            deleted_url = self.cursor.fetchone()

            if deleted_url:
                # Proceed to delete the URL if it exists
                self.cursor.execute(""" DELETE FROM bookmarks WHERE id=? """, (self.url_id,))
                self.db.commit()
                return True
            else:
                print(f"\nError: No URL found with ID `{self.url_id}`. Nothing was deleted.")
                return False
        except sqlite3.OperationalError as e:
            print(f"\nDatabase error occurred: {str(e)}")
            return False
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            return False

    def update_url(self, url_id, new_url):
        """
        URLs can be updated with respect to id.
        """

        try:
            self.url_id = url_id
            self.new_url = new_url
        
            # Check if the record with the given id exists
            self.cursor.execute(""" SELECT url FROM bookmarks WHERE id=?""", (self.url_id,))
            current_url = self.cursor.fetchone()

            if current_url[0] != new_url:
                # Perform the update
                self.cursor.execute(
                    """ UPDATE bookmarks SET url=? WHERE id=?""", (self.new_url, self.url_id)
                )
                self.db.commit()
                return True
            else:
                print("\nSuccess: The provided URL is already bookmarked. No changes were made.")
                return False

        except sqlite3.OperationalError as e:
            print(f"\nERROR: Failed to update URL. {str(e)}")
            return False
        except Exception as e:
            print(f"\nError: An unexpected error occurred: {str(e)}")
            return False

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
                    (self.search),
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
            # Check if there are any URLs in the database before deleting
            self.cursor.execute(""" SELECT COUNT(*) FROM bookmarks """)
            url_count = self.cursor.fetchone()[0]

            if url_count > 0:
                # If URLs exist, proceed to delete all records
                self.cursor.execute(""" DELETE FROM bookmarks """)
                self.db.commit()
                print(f"\nSuccess: All {url_count} URLs have been successfully deleted.")
                return True
            else:
                print("\n Success: No URLs found in the database to delete.")
                return False
        except sqlite3.OperationalError as e:
            print(f"\nDatabase error occurred: {str(e)}")
            return False
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            return False

    def open_url(self, url_id_tag):
        """
        Opens the URLs in default browser.
        """
        try:
            all_row = self.check_id(url_id_tag)
            if not all_row:
                all_row = self.search_url(url_id_tag)
                for bookmark in all_row:
                    webbrowser.open(bookmark[1])
                self.db.commit()
                return True
            else:
                print("\nError: Provide either valid url id or url tag name or any valid substring.")

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
            self.cursor.execute(""" SELECT url FROM bookmarks WHERE id=?""", (url_id))
            all_row = self.cursor.fetchall()
            if all_row == []:
                return None
            return all_row
        except Exception:
            raise sqlite3.OperationalError

    @staticmethod
    def select_directory():
        # Function to open a directory dialog and select a folder
        # Create the root window
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        # Open directory dialog
        folder_path = filedialog.askdirectory(title="Select a folder")

        if folder_path:
            print(f"\nSelected folder: {folder_path}")
        else:
            print("\nNo folder selected")
        return folder_path

    def export_urls(self):
        """
        Export URLs from the database to a CSV file.
        Returns the path of the exported CSV file or a tuple with a failure message.
        """
        try:
            folder_path = self.select_directory()
            if not folder_path:
                folder_path = os.path.expanduser("~/.config/readit")

            if not os.path.exists(folder_path):
                msg = "File path does not exist: " + folder_path
                return False, msg
            
        except OSError as e:
            msg = f"Error: Finding directory: {str(e)}"
            return False, msg
        
        database_file = os.path.join(os.path.expanduser("~/.config/readit"), "bookmarks.db")
        try:
            # Ensure the database file exists
            db_file_paths = glob(os.path.expanduser(database_file))
            if not db_file_paths:
                return False, f"Error: Database file not found at: {database_file}"

            # Open the database connection and export to CSV
            with sqlite3.connect(db_file_paths[0]) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM bookmarks")
                
                # Export to CSV
                csv_file_path = os.path.join(folder_path, "exported_bookmarks.csv")
                with open(csv_file_path, "w", newline="") as csv_file:
                    csv_writer = csv.writer(csv_file, delimiter="\t")
                    csv_writer.writerow([i[0] for i in cursor.description])  # Headers
                    csv_writer.writerows(cursor)  # Data rows

                return csv_file_path
        
        except sqlite3.OperationalError as e:
            msg = f"Database operation failed: {str(e)}"
            return False, msg

        except Exception as e:
            msg = f"Unexpected error: {str(e)}"
            return False, msg

        exporter = BookmarkExporter()
        result = exporter.export_urls()
        if isinstance(result, tuple) and result[0] is False:
            print(result[1])  # Print error message
        else:
            print(f"Bookmarks exported successfully to: {result}")

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
