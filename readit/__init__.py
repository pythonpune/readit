"""
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
"""
import click

from readit.cli import add
from readit.cli import clear
from readit.cli import delete
from readit.cli import export
from readit.cli import insert
from readit.cli import openurl
from readit.cli import search
from readit.cli import tag
from readit.cli import taglist
from readit.cli import update
from readit.cli import urlinfo
from readit.cli import version
from readit.cli import view


@click.group()
def main():
    pass


main.add_command(add)
main.add_command(tag)
main.add_command(delete)
main.add_command(clear)
main.add_command(update)
main.add_command(search)
main.add_command(view)
main.add_command(openurl)
main.add_command(version)
main.add_command(export)
main.add_command(taglist)
main.add_command(urlinfo)
main.add_command(insert)

if __name__ == "__main__":

    """
    This is initial function.
    It calls the main function.
    """
    main()
