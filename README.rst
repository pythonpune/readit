**************************
Readit - Command Line Tool
**************************

.. class:: no-web no-pdf

|Python| |Licence| |Build Status| 

.. image:: https://asciinema.org/a/XHY1hKrgOry69OeWG04iucT1k.png
   :alt: asciicast
   :target: https://asciinema.org/a/XHY1hKrgOry69OeWG04iucT1k?t=1

Introduction
************
Readit is command line bookmark manager. It is a command line utility to add, delete, update and display the bookmarks. It is a powerful bookmark manager written in Python. It uses SQLite3 database to store the bookmarks.


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


Dependencies
************
=============================================      ==================
     Features                                       Dependancy
=============================================      ==================
``Scripting Language``                              Python 2.7+
``HTTP(S)``                                         requests
``Command-Line Option and argument parsing``        click
``Database Used``                                   SQLite3
``Display Bookmarks in Table``                      beautifultable
=============================================      ==================

Installation
************
readit is available on PyPi and can be installed with pip3:

.. code-block:: bash
	
	pip3 install --user readit

Command line options
********************
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


How to install source code for development 
**********************************************
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

`Licence <https://github.com/projectreadit/readit/blob/master/LICENSE>`_
***********************************************************************
Readit - Command line tool is licensed under `GNU General Public License v3.0. <https://github.com/projectreadit/readit/blob/master/LICENSE>`_

.. |Python| image:: https://img.shields.io/badge/python-2.7%2C%203.6-blue.svg

.. |Licence| image:: https://img.shields.io/badge/license-GPLv3-yellow.svg?maxAge=2592000
    :target: https://github.com/projectreadit/readit/blob/master/LICENSE

.. |Build Status| image:: https://travis-ci.org/projectreadit/readit.svg?branch=master
    :target: https://travis-ci.org/projectreadit/readit
