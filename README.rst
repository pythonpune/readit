**************************
Readit - Command Line Tool
**************************

.. class:: no-web no-pdf

|Python| |Licence| |Build Status| |docs passing|


Introduction
************
Readit is command line bookmark manager. It is a command line utility to add, delete, update and display the bookmarks. It is a powerful bookmark manager written in Python. It uses SQLite3 database to store the bookmarks.


Features
********
* Bookmark multiple URLs at a time
* Bookmark URL with respective Tags at the same time [NEW]
* Search and display Bookmarks by TAG and URL's substring
* Display all Bookmarks in table format
* Remove single or all Bookmarked URL
* Update a Bookmarked URL with a specific ID
* URL validation
* Open multiple URLs in the browser
* Choose specific folder and Export bookmarks into the CSV file [NEW]
* Show all Tags available in the database
* Bookmark URLs either online or offline


Dependencies
************
=============================================      ==================
    Features                                       Dependancy
=============================================      ==================
``Scripting Language``                              Python 3.0+
``HTTP(S)``                                         requests
``Command-line parsing``                            click
``Database``                                        SQLite3
``Display Bookmarks in Table``                      beautifultable
=============================================      ==================

Installation
************
Readit is available on PyPI and can be installed with pip3:

.. code-block:: bash

    pip3 install --user readit

Command line options
********************
.. code-block:: bash

    Usage: readit [OPTIONS] [INSERT]...

        Readit - Command-line bookmark manager tool.
    Options:
    -a, --add TEXT          Add urls --> readit -a <url1> <url2>
    -t, --tag TEXT          Use to tag url --> readit -a <url1> -t <tag1>
    -d, --delete TEXT       Remove a URL of particular ID --> readit -d <url_id>
    -c, --clear TEXT        Clear bookmarks --> readit -c
    -u, --update TEXT       Update a URL for specific ID --> readit -u
                            <existing_id> <new_url>
    -s, --search TEXT       Search for bookmarks using either a tag or a
                            substring of the URL --> readit -s <tag> or
                            <substring>
    -v, --view TEXT...      Show bookmarks --> readit -v
    -o, --openurl TEXT      Open a URL in your browser by entering a part of the
                            URL. --> readit -o <url_substring>
    -V, --version           Check latest version --> readit -V
    -e, --export TEXT...    Export URLs in csv file --> readit -e
    -tl, --taglist TEXT...  Show all Tags --> readit -tl
    --help                  Show this message and exit.


Examples
********
1. **Bookmark** multiple URLs:

.. code-block:: bash

    $ readit <url1> <url2> ...
    or
    $ readit --add <url1> <url2> ...
    or
    $ readit -a <url1> <url2> ...

2. **Bookmark** urls and tags at the same time

.. code-block:: bash

    $ readit -a <url1> -t <tag1>

2. **View** all available bookmarks:

.. code-block:: bash

    $ readit -v
    or
    $ readit --view

3. **Update** a bookmark using its ID:

.. code-block:: bash

    $ readit -u <url_id> <url>
    or
    $ readit --update <url_id> <url>

4. **Delete** a bookmarked URL using its ID:

.. code-block:: bash

    $ readit -d <url_id>
    or
    $ readit --delete <url_id>

5. **Clear** all the bookmarks:

.. code-block:: bash

    $ readit -c
    or
    $ readit --clear

6. **Search** and **Display** all bookmarks using the TAG or URL's substring:

.. code-block:: bash

    $ readit -s <tag_name> or <url_substring>
    or
    $ readit --search <tag_name> or <url_substring>

7. Open URL in the Browser using URL's substring:

.. code-block:: bash

    $ readit -o <url_substring>
    or
    $ readit --openurl <url_substring>

8. **Export** bookmarks into the CSV file:

.. code-block:: bash

    $ readit --export
    or
    $ readit -e

9. Show all Tags available in the database

.. code-block:: bash

    $ readit -tl
    or
    $ readit --taglist

How to install source code for development
**********************************************
* Clone project from github:

.. code-block:: bash

    $ git clone https://github.com/pythonpune/readit.git

* We recommend to create and activate a virtualenv first:

.. code-block:: bash

    $ cd readit/

    $ python3 -m venv env

    $ source env/bin/activate

    $ pip3 install setuptools

* To install using setup.py file:

.. code-block:: bash

        (env) $ python setup.py install

* To make a build of the project:

.. code-block:: bash

        (env) $ python setup.py build

************************************************************************
`Licence <https://github.com/pythonpune/readit/blob/master/LICENSEE>`_
************************************************************************
Readit - Command line tool is licensed under `GNU General Public License v3.0. <https://github.com/pythonpune/readit/blob/master/LICENSE>`_

.. |Python| image:: https://img.shields.io/badge/python-3.6-blue.svg

.. |Licence| image:: https://img.shields.io/badge/license-GPLv3-yellow.svg?maxAge=2592000
    :target: https://github.com/pythonpune/readit/blob/master/LICENSE

.. |Build Status| image:: https://travis-ci.org/pythonpune/readit.svg?branch=master
    :target: https://travis-ci.org/pythonpune/readit

.. |docs passing| image:: https://readthedocs.org/projects/readit/badge/?version=latest
    :target: http://readittool.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
