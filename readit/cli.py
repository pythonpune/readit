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
import sys  # used to exit from system

import click  # used for command line interface.
import requests  # to check whether url is valid or not

from readit import database  # used to perform database operations.
from readit import view  # Used to show results to users

database_connection = database.DatabaseConnection()
output = view.ShowResults()


@click.command()
@click.option("--add", "-a", nargs=0, help="Add URLs with space-separated")
@click.option("--tag", "-t", nargs=2, help="Add Tag with space-separated URL")
@click.option("--delete", "-d", nargs=1, help="Remove a URL of particular ID")
@click.option("--clear", "-c", multiple=True, nargs=0, help="Clear bookmarks")
@click.option("--update", "-u", nargs=2, help="Update a URL for specific ID")
@click.option("--search", "-s", nargs=1, help="Search for bookmarks using either a tag or a substring of the URL")
@click.option("--view", "-v", multiple=True, nargs=0, help="Show bookmarks")
@click.option("--openurl", "-o", nargs=1, help="Open a URL in your browser by entering a part of the URL.")
@click.option("--version", "-V", is_flag=True, help="Check latest version")
@click.option("--export", "-e", multiple=True, nargs=0, help="Export URLs in csv file")
@click.option("--taglist", "-tl", multiple=True, nargs=0, help="Show all Tags")
@click.argument("insert", nargs=-1, required=False)
def main(
    insert,
    add,
    tag,
    delete,
    clear,
    update,
    search,
    view,
    openurl,
    version,
    export,
    taglist,
):
    """
    Readit - Command-line bookmark manager tool.
    """
    if add:
        for url_to_add in add:
            url = url_to_add.strip()  # Strip any leading/trailing whitespace
            try:
                validate_url = requests.get(url)
                validate_code = validate_url.status_code
                if validate_code == 200:
                    is_url_added = database_connection.add_url(url)
                    if is_url_added:
                        print(f"\nSuccess: The URL '{url}' has been added to the database.")
                else:
                    print("*" * 12, "\nInvalid URL\n", "*" * 11)
                    if option_yes_no():
                        is_url_added = database_connection.add_url(url)
                        if is_url_added:
                            print(f"\nSuccess: The URL '{url}' has been added to the database.")
            except Exception:
                print("*" * 12, "\nInvalid URL\n", "*" * 11)
                if option_yes_no():
                    is_url_added = database_connection.add_url(url)
                    if is_url_added:
                        print(f"\nSuccess: The URL '{url}' has been added to the database.")
    elif delete:
        database_connection.delete_url(delete)            
    elif update:
        url_list = []
        for update_to_url in update:
            url_list.append(update_to_url)
        url_id = url_list[0]
        url = url_list[1].strip()  # Strip any leading/trailing whitespace
        try:
            validate_url = requests.get(url)
            validate_code = validate_url.status_code
            if validate_code == 200:
                database_connection.update_url(url_id, url)
            else:
                print("*" * 12, "\nInvalid URL\n", "*" * 11)
                if option_yes_no():
                    database_connection.update_url(url_id, url)
        except Exception:
            print("*" * 12, "\nInvalid URL\n", "*" * 11)
            if option_yes_no():
                is_url_updated = database_connection.update_url(url_id, url)
                if is_url_updated:
                    print(f"\nSuccess: URL of ID {url_id} updated.")
    elif view:
        output.print_bookmarks(database_connection.show_urls())
    elif openurl:
        database_connection.open_url(openurl)
    elif search:
        output.print_bookmarks(database_connection.search_url(search))
    elif clear:
        database_connection.delete_all_url()
    elif tag:
        tag_list = []
        for tag_to_url in tag:
            tag_list.append(tag_to_url)
        tag_name = tag_list[0]
        tagged_url = tag_list[1].strip()  # Strip any leading/trailing whitespace
        try:
            validate_url = requests.get(tagged_url)
            validate_code = validate_url.status_code
            if validate_code == 200:
                is_url_tagged = database_connection.tag_url(tag_name, tagged_url)
                if is_url_tagged:
                    print(f"\nSuccess: Bookmarked URL `{tagged_url}` with tag `{tag_name}`.")
            else:
                print("*" * 12, "\nInvalid URL\n", "*" * 11)
                if option_yes_no():
                    is_url_tagged = database_connection.tag_url(tag_name, tagged_url)
                    if is_url_tagged:
                        print(f"\nSuccess: Bookmarked URL `{tagged_url}` with tag `{tag_name}`.")
        except Exception:
            print("*" * 12, "\nInvalid URL\n", "*" * 11)
            if option_yes_no():
                is_url_tagged = database_connection.tag_url(tag_name, tagged_url)
                if is_url_tagged:
                    print(f"\nSuccess: Bookmarked URL `{tagged_url}` with tag `{tag_name}`.")
    elif taglist:
        output.print_all_tags(database_connection.list_all_tags())
    elif version:
        print("readit v0.3")
    elif export:
        path = database_connection.export_urls()
        if path:
            print(f"\nExported bookmarks available at `{path}`")
        else:
            print("\nError: Bookmarks are not exported in csv file.")
    else:
        for url_to_add in insert:
            url = url_to_add.strip()  # Strip any leading/trailing whitespace
            try:
                validate_url = requests.get(url)
                validate_code = validate_url.status_code
                if validate_code == 200:
                    is_url_added = database_connection.add_url(url)
                    if is_url_added:
                        print(f"\nSuccess: The URL '{url}' has been added to the database.")
                else:
                    print("*" * 12, "\nInvalid URL\n", "*" * 11)
                    if option_yes_no():
                        is_url_added = database_connection.add_url(url)
                        if is_url_added:
                            print(f"\nSuccess: The URL '{url}' has been added to the database.")

            except Exception:
                print("*" * 12, "\nInvalid URL\n", "*" * 11)
                if option_yes_no():
                    is_url_added = database_connection.add_url(url)
                    if is_url_added:
                        print(f"\nSuccess: The URL '{url}' has been added to the database.")

def option_yes_no():
    """
    Asks whether to bookmark invalid URLs or Offline URLs to database.
    """
    option = input("Still you want to bookmark: Yes/No ? ")
    if option.lower() in ["yes", "y"]:
        return True
    else:
        sys.exit(0)
