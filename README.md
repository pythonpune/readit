# Readit - Command line tool


## Introduction
Readit is command line bookmark manager. It is a command line utility to add, delete, update the bookmarks. It is a powerful bookmark manager written in Python3 and SQLite3.

## Features

  - Add multiple links at a time
  - Delete a link
  - Update a link
  - Link validation while adding

#### Dependencies

| Feature | Dependency |
| --- | --- |
| Scripting language | Python 2.7+ |
| HTTP(S) | Requests |
| Command-Line Option and Argument Parsing  | Click |
| Database used  | SQLite |


#### Command line options

```
Usage: readit [OPTIONS] [INSERT]...

  It performs database operations as per arguments passed by user.

Options:
  -a, --add TEXT        add url
  -d, --delete TEXT    delete url
  -c, --clear TEXT...   Clear database
  -u, --update TEXT   update url
  -v, --view TEXT...    show url
  --help                     Show this message and exit.

```

#### Examples


1. **Add**  bookmarks:

       $ readit -a https://www.google.co.in/
       or
       $ readit --add https://www.github.com
       or
       $ readit https://www.google.co.in/ https://github.com/
       or
       readit -a https://www.google.co.in/ -a https://github.com/
       or
       readit --add https://www.google.co.in/ --add https://github.com/

       
2. **View** all available bookmarks:

       $ readit -v
       or 
       $ readit --view

      
3. **Update** a bookmark using it's ID:

       $ readit -u 1 -u https://www.google.co.in/
       or
       $ readit --update 1 --update https://www.google.co.in/

     
4. **Delete** a bookmarked link using it's ID:

       $ readit -d 1
       or
       $ readit --delete 1 
       
       
5. **Clear** all the bookmarks:

       $ readit -c
       or
       $ readit --clear



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



