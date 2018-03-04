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

import requests  # to check whether url is valid or not
import click  # used for command line interface.
from readit import database  # used to perform database operations.


@click.command()
@click.option('--add', '-a', nargs=0, help="Add URLs with space-separated")
@click.option('--tag', '-t', nargs=2, help="Add Tag with space-separated URL")
@click.option('--delete', '-d', nargs=1, help="Remove a URL of particular ID")
@click.option('--clear', '-c', multiple=True, nargs=0, help="Clear bookmarks")
@click.option('--update', '-u', nargs=2, help="Update a URL for specific ID")
@click.option('--search', '-s', nargs=1, help="Search all bookmarks by Tag")
@click.option('--view', '-v', multiple=True, nargs=0, help="Show bookmarks")
@click.option('--openurl', '-o', nargs=1, help="Open URL in Browser")
@click.option('--version', '-V', is_flag=True, help="Check latest version")
@click.argument('insert', nargs=-1, required=False)
def main(insert, add, tag, delete, clear,
         update, search, view, openurl, version):
    """
    Readit - Command-line bookmark manager tool.
    """
    database_connection = database.DatabaseConnection()

    if add:
        for url_to_add in add:
            url = url_to_add
            try:
                validate_url = requests.get(url)
                validate_code = validate_url.status_code
                if validate_code == 200:
                    database_connection.add_url(url)
                else:
                    print("Invalid URL:--> ", url)
            except Exception as e:
                print("Invalid input:--> ", e)

    elif delete:
        database_connection.delete_url(delete)

    elif update:
        url_list = []
        for update_to_url in update:
            url_list.append(update_to_url)
        url_id = url_list[0]
        url = url_list[1]
        try:
            validate_url = requests.get(url)
            validate_code = validate_url.status_code
            if validate_code == 200:
                database_connection.update_url(url_id, url)
            else:
                print("Invalid URL:--> ", url)
        except Exception as e:
            print("Invalid input:-->  ", e)

    elif view:
        database_connection.show_url()
    elif openurl:
        database_connection.open_url(openurl)
    elif search:
        database_connection.search_by_tag(search)
    elif clear:
        database_connection.delete_all_url()
    elif tag:
        tag_list = []
        for tag_to_url in tag:
            tag_list.append(tag_to_url)
        tag_name = tag_list[0]
        tagged_url = tag_list[1]
        try:
            validate_url = requests.get(tagged_url)
            validate_code = validate_url.status_code
            if validate_code == 200:
                database_connection.tag_url(tag_name, tagged_url)
            else:
                print("Invalid URL:-->", tagged_url)
        except Exception as t:
            print("Invalid input:--> ", t)
    elif version:
        print("readit v0.1.1")
    else:
        for url_to_add in insert:
            url = url_to_add
            try:
                validate_url = requests.get(url)
                validate_code = validate_url.status_code
                if validate_code == 200:
                    database_connection.add_url(url)
                else:
                    print("Invalid URL:--> ", url)
            except Exception as e:
                print("Invalid input:-->  ", e)
