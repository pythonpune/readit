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
from beautifultable import BeautifulTable  # Used to create table formats

table = BeautifulTable()
table_tag = BeautifulTable()
table.columns.header = ["ID", "URL", "TAG", "DATE", "TIME"]
table_tag.columns.header = ["Available Tags"]


class ShowResults(object):
    """This class includes methods. Which are used to
    show output to the user in table format.
    """

    def __init__(self):
        pass

    def print_all_tags(self, tag_list):
        if tag_list:
            print("\033[34m\n*Collection of associated Tags.*\033[0m\n")
            for tag_in_list in tag_list:
                table_tag.rows.append([tag_in_list])
            print(table_tag)
        else:
            print("\033[92m\nSuccess: Tags list is empty.\033[0m")

    def print_bookmarks(self, all_bookmarks):
        if all_bookmarks:
            print("\033[34m\n*Collection of Bookmarked Links*\033[0m\n")
            for bookmark in all_bookmarks:
                table.rows.append([bookmark[0], bookmark[1], bookmark[2], bookmark[3], bookmark[4]])
            print(table)
        else:
            print("\033[92m\nSuccess: No bookmarks found.\033[0m")
