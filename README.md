# Readit - Command Line Tool

[![Python](https://img.shields.io/badge/python-2.7%2C%203.6-blue.svg)]() [![LICENSE](https://img.shields.io/badge/license-GPLv3-yellow.svg?maxAge=2592000)]() [![Build Status](https://travis-ci.org/freeCodeCamp/how-to-contribute-to-open-source.svg?branch=master)](https://travis-ci.org/freeCodeCamp/how-to-contribute-to-open-source)

## Introduction

Readit is command line bookmark manager. It is a command line utility to add, delete, update and display the bookmarks. It is a powerful bookmark manager written in Python. It uses SQLite3 to store the bookmarks.

## Features

  - Bookmark multiple URLs at a time
  - Bookmark URL with respective Tags
  - Search and display Bookmarks by TAG
  - Display all Bookmarks in table format
  - Remove a Bookmarked URL
  - Remove all Bookmarked URLs 
  - Update a Bookmarked URL with specific ID
  - URL validation
  - Open URL in browser 

#### Dependencies

| Feature | Dependency |
| --- | --- |
| Scripting language | Python 2.7+ |
| HTTP(S) | Requests |
| Command-Line Option and Argument Parsing  | Click |
| Database used  | SQLite3 |
| Display Bookmarks in Table | beautifultable |


#### Command line options

```
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
```

#### Examples


1. **Bookmark** multiple URLs:

       $ readit url1 url2 ...
       or
       $ readit --add url1 url2 ...
       or
       $ readit -a url1 url2 ...

       
2. **View** all available bookmarks:

       $ readit -v
       or 
       $ readit --view

      
3. **Update** a bookmark using it's ID:

       $ readit -u url_id url
       or
       $ readit --update url_id url

     
4. **Delete** a bookmarked URL using it's ID:

       $ readit -d url_id
       or
       $ readit --delete url_id 
       
       
5. **Clear** all the bookmarks:

       $ readit -c
       or
       $ readit --clear

6. **Bookmark URL with TAG**:
 
       $ readit -t tag_name url
       or
       $ readit --tag tag_name url

7. **Search and Display** all bookmarks using TAG:
      
       $ readit -s tag_name 
       or
       $ readit --search tag_name

8. **Open** URL in Browser using specific ID:

       $ readit -o urlid
       or
       $ readit --openurl urlid

#### How to Install
-----------------

* Clone project from github:
```
  $ git clone https://github.com/ganeshhubale/readit.git
```

* We recommend to create and activate a virtualenv first:
```
  $ cd readit/
  
  $ virtualenv venv 

  $ source venv/bin/activate
  	
  (venv) $
```

* To install using setup.py file:
```	
	(venv) $ python setup.py install
```

* To make build of project:
```
	(venv) $ python setup.py build
```	

    
 
#### [License](https://github.com/ganeshhubale/readit/blob/master/LICENSE)
----

Readit - Command line tool is licensed under [GNU General Public License v3.0](https://github.com/ganeshhubale/readit/blob/master/LICENSE).



