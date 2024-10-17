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
        for url in add:
            try:
                validate_code = check_url_validation(url)
    
                if validate_code == 200:
                    is_url_added = database_connection.add_url(url)
                    if is_url_added:
                        print(f"\033[92m\nSuccess: The URL '{url}' has been added to the database.\033[0m")
                else:
                    print("\033[93m\nWarning: The URL seems to be inaccessible at the moment.\033[0m")  # Warning in yellow
                    if option_yes_no():
                        is_url_added = database_connection.add_url(url)
                        if is_url_added:
                            print(f"\033[92m\nSuccess: The URL '{url}' has been added to the database.\033[0m")
            except Exception:
                print("\033[93m\nWarning: The URL seems to be inaccessible at the moment.\033[0m")  # Warning in yellow
                if option_yes_no():
                    is_url_added = database_connection.add_url(url)
                    if is_url_added:
                        print(f"\033[92m\nSuccess: The URL '{url}' has been added to the database.\033[0m")
    elif delete:
        database_connection.delete_url(delete)            
    elif update:
        url_list = []
        for update_to_url in update:
            url_list.append(update_to_url)
        url_id = url_list[0]
        url = url_list[1]
        try:
            validate_code = check_url_validation(url)

            if validate_code == 200:
                database_connection.update_url(url_id, url)
            else:
                print("\033[93m\nWarning: The URL seems to be inaccessible at the moment.\033[0m")  # Warning in yellow
                if option_yes_no():
                    database_connection.update_url(url_id, url)
        except Exception:
            print("\033[93m\nWarning: The URL seems to be inaccessible at the moment.\033[0m")  # Warning in yellow
            if option_yes_no():
                is_url_updated = database_connection.update_url(url_id, url)
                if is_url_updated:
                    print(f"\033[92m\nSuccess: URL of ID {url_id} updated.\033[0m")
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
        tagged_url = tag_list[1]
        try:
            validate_code = check_url_validation(tagged_url)
            if validate_code == 200:
                is_url_tagged = database_connection.tag_url(tag_name, tagged_url)
                if is_url_tagged:
                    print(f"\033[92m\nSuccess: Bookmarked URL `{tagged_url}` with tag `{tag_name}`.\033[0m")
            else:
                print("\033[93m\nWarning: The URL seems to be inaccessible at the moment.\033[0m")  # Warning in yellow
                if option_yes_no():
                    is_url_tagged = database_connection.tag_url(tag_name, tagged_url)
                    if is_url_tagged:
                        print(f"\033[92m\nSuccess: Bookmarked URL `{tagged_url}` with tag `{tag_name}`.\033[0m")
        except Exception:
            print("\033[93m\nWarning: The URL seems to be inaccessible at the moment.\033[0m")  # Warning in yellow
            if option_yes_no():
                is_url_tagged = database_connection.tag_url(tag_name, tagged_url)
                if is_url_tagged:
                    print(f"\033[92m\nSuccess: Bookmarked URL `{tagged_url}` with tag `{tag_name}`.\033[0m")
    elif taglist:
        output.print_all_tags(database_connection.list_all_tags())
    elif version:
        print("\033[92m\nreadit v0.3 \033[0m")
    elif export:
        path = database_connection.export_urls()
        if path:
            print(f"\033[92m\nSuccess: Exported bookmarks available at `{path}`.\033[0m")
        else:
            print("\033[91m\nError: Bookmarks are not exported in csv file.\033[0m")
    else:
        for url in insert:
            try:
                validate_code = check_url_validation(url)

                if validate_code == 200:
                    is_url_added = database_connection.add_url(url)
                    if is_url_added:
                        print(f"\033[92m\nSuccess: The URL '{url}' has been added to the database.\033[0m")
                else:
                    print("\033[93m\nWarning: The URL seems to be inaccessible at the moment.\033[0m")  # Warning in yellow
                    if option_yes_no():
                        is_url_added = database_connection.add_url(url)
                        if is_url_added:
                            print(f"\033[92m\nSuccess: The URL '{url}' has been added to the database.\033[0m")

            except Exception:
                print("\033[93m\nWarning: The URL seems to be inaccessible at the moment.\033[0m")  # Warning in yellow
                if option_yes_no():
                    is_url_added = database_connection.add_url(url)
                    if is_url_added:
                        print(f"\033[92m\nSuccess: The URL '{url}' has been added to the database.\033[0m")

def option_yes_no():
    """
    Asks whether to bookmark invalid URLs or Offline URLs to database.
    """
    option = input("\033[96m\nAre you sure you want to bookmark this URL? (Yes/No) \033[0m")
    if option.lower() in ["yes", "y"]:
        return True
    else:
        sys.exit(0)

def check_url_validation(url_given):
    url = url_given.strip()  # Strip any leading/trailing whitespace
    if not url:
        print("\033[91m\nError: Cannot add an empty URL.\033[0m")
        sys.exit(0)
    
    # Initialize the validation code
    validate_code = 0

    if not url.startswith(("http://", "https://")):
        # First try with http, if it fails, try https
        for prefix in ["http://", "https://"]:
            full_url = prefix + url
            response = requests.get(full_url)
            if response.status_code == 200:
                validate_code = 200
                url = full_url  # Update URL with valid prefix
                break
        else:
            validate_code = 0 
    else:
        # If URL starts with http or https, validate directly
        response = requests.get(url)
        validate_code = response.status_code
    return validate_code