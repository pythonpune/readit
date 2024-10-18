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
                # Create bookmarks table
                self.cursor.execute(
                    """CREATE TABLE IF NOT EXISTS bookmarks
                    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    url TEXT UNIQUE NOT NULL, date TEXT, time TEXT)"""
                )

                # Create tags table
                self.cursor.execute(
                    """CREATE TABLE IF NOT EXISTS tags
                    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    tag_name TEXT UNIQUE NOT NULL)"""
                )

                # Create url_tags table (junction table for many-to-many relationship)
                self.cursor.execute(
                    """CREATE TABLE IF NOT EXISTS url_tags
                    (url_id INTEGER NOT NULL,
                    tag_id INTEGER NOT NULL,
                    FOREIGN KEY (url_id) REFERENCES bookmarks(id),
                    FOREIGN KEY (tag_id) REFERENCES tags(id),
                    PRIMARY KEY (url_id, tag_id))"""
                )
                self.db.commit()
            else:
                raise IOError("\nDirectory does not exists")
        except sqlite3.OperationalError as e:
            print("\033[91m\nERROR: Failed to create table in the database.\033[0m")
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
            global date
            start = datetime.datetime.now()
            time = start.strftime("%H:%M:%S")

            self.cursor.execute(
                """
                INSERT INTO bookmarks(url, date, time) VALUES (?, ?, ?)
                """,
                (url, date, time),
            )
            self.db.commit()
            return True

        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                print(f"\033[91m\nError: The URL '{url}' already bookmarked.\033[0m")
                return False
            else:
                print(f"\nDatabase error: {str(e)}")
                return False

        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            return False

    def tag_url(self, tagged_url, tag_name):
        """
        URLs can be tagged with multiple tags.
        If the URL already exists, associate it with the new tag.
        """
        self.tag = tag_name.lower()
        self.url = tagged_url

        try:
            # Initialize date and time
            start = datetime.datetime.now()
            date = start.strftime("%Y-%m-%d")
            time = start.strftime("%H:%M:%S")

            # Insert the URL into bookmarks if it doesn't exist
            self.cursor.execute("SELECT id FROM bookmarks WHERE url=?", (self.url,))
            url_row = self.cursor.fetchone()
            if not url_row:
                # If URL does not exist, insert it
                self.cursor.execute(
                    """INSERT INTO bookmarks(url, date, time)
                    VALUES(?, ?, ?)""",
                    (self.url, date, time),
                )
                url_id = self.cursor.lastrowid
            else:
                url_id = url_row[0]

            # Insert the tag into tags table if not already present
            self.cursor.execute("SELECT id FROM tags WHERE tag_name=?", (self.tag,))
            tag_row = self.cursor.fetchone()

            if not tag_row:
                # If tag does not exist, insert it
                self.cursor.execute("""INSERT INTO tags(tag_name) VALUES(?)""", (self.tag,))
                tag_id = self.cursor.lastrowid
            else:
                tag_id = tag_row[0]

            # Link the URL and tag in the url_tags table
            self.cursor.execute(
                """INSERT OR IGNORE INTO url_tags(url_id, tag_id)
                VALUES(?, ?)""",
                (url_id, tag_id),
            )

            self.db.commit()
            return True

        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                print(
                    f"""\033[91m\nError: The URL '{self.url}'
                    has already been taggedwith '{self.tag}'.\033[0m"""
                )
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
        try:
            # Query to get all tags
            self.cursor.execute("""SELECT tag_name FROM tags""")
            tags_in_db = self.cursor.fetchall()

            # Extract tag names from the result tuples and sort them
            tag_list = [tag[0] for tag in tags_in_db]
            tag_list.sort()

            return tag_list

        except sqlite3.OperationalError as e:
            print(f"\nDatabase error occurred: {str(e)}")
            return []

        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            return []

    def delete_url(self, url_id):
        """
        Deletes the URL and its associated tags
        (from the url_tags table) based on the provided URL ID.
        """
        try:
            self.url_id = url_id

            # Check if the URL exists before attempting to delete
            self.cursor.execute("""SELECT url FROM bookmarks WHERE id=?""", (self.url_id,))
            deleted_url = self.cursor.fetchone()

            if deleted_url:
                # Delete the associated entries from url_tags table
                self.cursor.execute("""DELETE FROM url_tags WHERE url_id=?""", (self.url_id,))

                # Delete the URL from bookmarks table
                self.cursor.execute("""DELETE FROM bookmarks WHERE id=?""", (self.url_id,))

                # Commit the transaction
                self.db.commit()

                print(
                    f"""\033[92m\nSuccessfully deleted URL '{deleted_url[0]}' and
                    its associated tags.\033[0m"""
                )
                return True
            else:
                print(
                    f"""\033[91m\nError: No URL found with ID `{self.url_id}`.
                    Nothing was deleted.\033[0m"""
                )
                return False

        except sqlite3.OperationalError as e:
            print(f"\nDatabase error occurred: {str(e)}")
            return False

        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            return False

    def update_url(self, url_id, new_url):
        """
        Updates the URL with respect to the given ID.
        """
        try:
            self.url_id = url_id
            self.new_url = new_url

            # Check if the record with the given id exists
            self.cursor.execute("""SELECT url FROM bookmarks WHERE id=?""", (self.url_id,))
            current_url = self.cursor.fetchone()

            if current_url:
                # If the new URL is different from the existing one, update it
                if current_url[0] != new_url:
                    self.cursor.execute(
                        """UPDATE bookmarks SET url=? WHERE id=?""", (self.new_url, self.url_id)
                    )
                    self.db.commit()
                    print(f"\033[92m\nSuccess: URL updated to '{self.new_url}'.\033[0m")
                    return True
                else:
                    print(
                        """\033[92m\nNo changes: The provided URL is already bookmarked.
                        No update needed.\033[0m"""
                    )
                    return False
            else:
                print(
                    f"""\033[91m\nError: No URL found with ID `{self.url_id}`.
                    Update failed.\033[0m"""
                )
                return False

        except sqlite3.OperationalError as e:
            print(f"\nERROR: Failed to update URL. {str(e)}")
            return False

        except Exception as e:
            print(f"\nError: An unexpected error occurred: {str(e)}")
            return False

    def show_urls(self):
        """
        Fetches all URLs along with their associated tags, date, and
        time from the database.
        """
        try:
            # Join bookmarks with url_tags and tags to fetch the required data
            query = """
                SELECT b.id, b.url, t.tag_name, b.date, b.time
                FROM bookmarks AS b
                LEFT JOIN url_tags AS ut ON b.id = ut.url_id
                LEFT JOIN tags AS t ON ut.tag_id = t.id
            """
            self.cursor.execute(query)
            all_bookmarks = self.cursor.fetchall()
            self.db.commit()

            if not all_bookmarks:
                return None
            else:
                return all_bookmarks

        except sqlite3.OperationalError as e:
            print(f"\nERROR: Database operation failed: {str(e)}")
            return None
        except Exception as e:
            print(f"\nERROR: An unexpected error occurred: {str(e)}")
            return None

    def search_url(self, search_value):
        """
        Displays a group of URLs associated with the provided
        search_value (tag or url substring).
        """
        try:
            self.search = search_value.lower()
            all_bookmarks = []

            # Search for URLs directly by tag
            self.cursor.execute(
                """
                SELECT b.id, b.url, t.tag_name, b.date, b.time
                FROM bookmarks AS b
                JOIN url_tags AS ut ON b.id = ut.url_id
                JOIN tags AS t ON ut.tag_id = t.id
                WHERE t.tag_name = ?
            """,
                (self.search,),
            )  # Use a tuple with a trailing comma
            all_bookmarks = self.cursor.fetchall()

            if not all_bookmarks:
                # If no bookmarks found with the tag, search in all URLs by given value as substring
                bookmarks = self.show_urls()  # Fetch all URls
                for bookmark in bookmarks:
                    if self.search in bookmark[1].lower():  # Case-insensitive match
                        all_bookmarks.append(bookmark)

            self.db.commit()

            if not all_bookmarks:
                return None
            else:
                return all_bookmarks

        except sqlite3.OperationalError as e:
            print(f"\nERROR: Database operation failed: {str(e)}")
            return None
        except Exception as e:
            print(f"\nERROR: An unexpected error occurred: {str(e)}")
            return None

    def delete_all_url(self):
        """
        Delete all URLs and associated tags from the database.
        """
        try:
            # Check if there are any URLs in the database before deleting
            self.cursor.execute("""SELECT COUNT(*) FROM bookmarks""")
            url_count = self.cursor.fetchone()[0]

            if url_count > 0:
                # If URLs exist, proceed to delete all records
                self.cursor.execute("""DELETE FROM bookmarks""")
                self.cursor.execute(
                    """DELETE FROM url_tags"""
                )  # Delete all associations in the junction table
                self.cursor.execute(
                    """DELETE FROM tags WHERE tag_name NOT IN (SELECT tag_name FROM url_tags)"""
                )  # Delete orphaned tags
                self.db.commit()
                print(
                    f"""\033[92m\nSuccess: All {url_count} URLs and
                    their associated tags have been successfully deleted.\033[0m"""
                )
                return True
            else:
                print("\033[92m\nSuccess: No URLs found in the database to delete.\033[0m")
                return False

        except sqlite3.OperationalError as e:
            print(f"\nDatabase error occurred: {str(e)}")
            return False
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            return False

    def open_url(self, part_of_url):
        """
        Open a URL in your browser by entering a part of the URL.
        """
        try:
            urls = self.search_url(part_of_url)
            if urls:
                # Prompt the user before opening multiple URLs
                print(
                    f"""\033[96m\nFound {len(urls)} URLs.
                    Do you want to open them all? (yes/no) \033[0m"""
                )
                user_confirmation = input().strip().lower()

                if user_confirmation in ["yes", "y"]:
                    for url in urls:
                        url_to_open = url[1]  # Assuming url[1] contains the actual URL
                        try:
                            webbrowser.open(url_to_open)
                            print(f"Opening: {url_to_open}")
                        except Exception as e:
                            print(f"Could not open {url_to_open}: {str(e)}")
                else:
                    print("\033[92m\nOperation cancelled. No URLs were opened.\033[0m")
                self.db.commit()
                return True
            else:
                print("\033[91m\nError: Please enter a valid URL substring to proceed.\033[0m")

        except sqlite3.OperationalError as e:
            print(f"\nDatabase error occurred: {str(e)}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")

    @staticmethod
    def select_directory():
        # Function to open a directory dialog and select a folder
        # Create the root window
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        # Open directory dialog
        folder_path = filedialog.askdirectory(title="Select a folder")

        if folder_path:
            print(f"\n\033[92mSelected folder: {folder_path}.\033[0m")
        else:
            print("\n\033[92mNo folder selected. No Bookmarks are exported.\033[0m")
            sys.exit(0)
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
                msg = f"\033[91m\nFile path does not exist: {folder_path}.\033[0m"
                return False, msg

        except OSError as e:
            msg = f"\033[91m\nError: Finding directory: {str(e)}.\033[0m"
            return False, msg

        database_file = os.path.join(os.path.expanduser("~/.config/readit"), "bookmarks.db")
        try:
            # Ensure the database file exists
            db_file_paths = glob(os.path.expanduser(database_file))
            if not db_file_paths:
                return False, f"\033[91mError: Database file not found at: {database_file}.\033[0m"

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
