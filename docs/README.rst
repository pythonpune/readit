Readit
======

.. class::

|Python| |Licence| |Build Status|

.. image:: https://asciinema.org/a/UcO8Ast5X94F3kNtCuew7yZb2.png
   :alt: asciicast
   :target: https://asciinema.org/a/UcO8Ast5X94F3kNtCuew7yZb2?t=1

   


Introduction
************
Readit is command line bookmark manager. It is a command line utility to add, delete, update and display the bookmarks. It is a powerful bookmark manager written in Python. It uses SQLite3 to store the bookmarks.



.. contents:: 



Features
********
* Bookmark multiple URLs at a time
* Bookmark URL with respective Tags
* Search and display Bookmarks by TAG
* Display all Bookmarks in table format
* Remove a Bookmarked URL
* Remove all Bookmarked URLs
* Update a Bookmarked URL with specific ID
* URL validation
* Open URL in browser

Installation
************

Dependencies
************
=============================================      ==================
     Features                                       Dependancy
=============================================      ==================
``Scripting Language``                              Python 2.7+
``HTTP(S)``                                         requests
``Command-Line Option and argument parsing``        Click
``Database Used``                                   SQLite3
``Display Bookmarks in Table``                      beautifultable
=============================================      ==================

From a package manager
**********************
* `PyPi <https://pypi.python.org/pypi/readit/0.1.1>`_ (pip3 install --user readit).


Release Packages
****************
Packages for Fedora are availabe with the `latest release <https://github.com/projectreadit/readit/releases/tag/v0.1.1>`_.


Usage
*****

Cmdline options
***************

.. code-block:: bash

        Usage: readit [OPTIONS] [INSERT]...

          Readit - Command-line bookmark manager tool.

        Options:
        -a, --add TEXT...     Add URLs with space-separated
        -t, --tag TEXT...     Add Tag with space-separated URL
        -d, --delete TEXT     Remove a URL of particular ID
        -c, --clear TEXT...   Clear bookmarks
        -u, --update TEXT...  Update a URL for specific ID
        -s, --search TEXT     Search all bookmarks by Tag
        -v, --view TEXT...    Show bookmarks
        -o, --openurl TEXT    Open URL in Browser
        -V, --version         Check latest version
        --help                Show this message and exit.





Examples
********
1. **Bookmark** multiple URLs:

.. code-block:: bash

        $ readit url1 url2 ...
        or
        $ readit --add url1 url2 ...
        or
        $ readit -a url1 url2 ...

2. **View** all available bookmarks:

.. code-block:: bash

        $ readit -v
        or
        $ readit --view

3. **Update** a bookmark using it's ID:

.. code-block:: bash

        $ readit -u url_id url
        or
        $ readit --update url_id url

4. **Delete** a bookmarked URL using it's ID:

.. code-block:: bash

        $ readit -d url_id
        or
        $ readit --delete url_id

5. **Clear** all the bookmarks:

.. code-block:: bash

        $ readit -c
        or
        $ readit --clear

6. **Bookmark** URL with TAG:

.. code-block:: bash

        $ readit -t tag_name url
        or
        $ readit --tag tag_name url


7. **Search** and **Display** all bookmarks using TAG:

.. code-block:: bash

        $ readit -s tag_name
        or
        $ readit --search tag_name

8. Open URL in Browser using specific ID:

.. code-block:: bash

        $ readit -o urlid
        or
        $ readit --openurl urlid

How to Contribute
*****************
* Clone project from github:

.. code-block:: bash

        $ git clone https://github.com/projectreadit/readit.git

* We recommend to create and activate a virtualenv first:

.. code-block:: bash

        $ cd readit/

        $ virtualenv venv

        $ source venv/bin/activate

        (venv) $

* To install using setup.py file:

.. code-block:: bash

                (venv) $ python setup.py install

* To make build of project:

.. code-block:: bash

                (venv) $ python setup.py build



Project Structure
*****************
* Flowchart
* Modules

Collaborators
*************
* `Daivshala Vighne <https://github.com/daivshala>`_
* `Ganesh Hubale <https://github.com/ganeshhubale>`_
* `Shital Mule <https://github.com/shitalmule04>`_


.. |Python| image:: https://img.shields.io/badge/python-2.7%2C%203.6-blue.svg

.. |Licence| image:: https://img.shields.io/badge/license-GPLv3-yellow.svg?maxAge=2592000
    :target: https://github.com/projectreadit/readit/blob/master/LICENSE

.. |Build Status| image:: https://travis-ci.org/projectreadit/readit.svg?branch=master
    :target: https://travis-ci.org/projectreadit/readit


