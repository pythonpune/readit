# Readit - Command line tool

## Introduction
Readit is command line bookmark manager. It is a command line utility to add, delete, update the bookmarks. It is a powerful bookmark manager written in Python3 and SQLite3.

## Features

  - Add multiple links at a time
  - Delete a link
  - Update a link
  - Checks whether link is valid or not while adding

#### Dependencies

| Feature | Dependency |
| --- | --- |
| Scripting language | Python 3.4+ |
| HTTP(S) | Requests |
| Command-Line Option and Argument Parsing  | Click |
| Database used  | SQLite |


#### Command line options

```
usage: readit.py [-h] [-dt] [-a A [A ...]] [-v] [-u U U] [-d D] [-q]
                 [default [default ...]]

positional arguments:
  default

optional arguments:
  -h, --help            show this help message and exit
  -dt, -drop            delete all bookmarks
  -a A [A ...], -add A [A ...]
                        add bookmarks
  -v, -view             view bookmarks
  -u U U, -update U U   Update bookmarks by id
  -d D, -delete D       delete bookmarks by id	
  -q, -quiet            quiet
```

#### Examples

1. **Add**  bookmarks:

       $ readit -a https://www.google.co.in/ https://www.facebook.com/
       or
       $ readit -all https://www.google.co.in/ https://www.facebook.com/
       or
       $ readit https://www.google.co.in/ https://www.facebook.com/
    
2. **Delete** a bookmark using it's ID:

       $ readit -delete 1 
       or
       $ readit -d 1  
    
3. **Delete all**  bookmarks:

       $ readit -drop
       or
       $ readit -dt 
       
4. **Update** a bookmark using it's ID:

       $ readit -u 1 https://www.google.co.in/
       or
       $ readit -update 1 https://www.google.co.in/ 
    
5. **View** all available bookmarks:

       $ readit -v
       or 
       $ readit -view
       
6. **To Quiet** from readit tool:

       $ readit -q
       or
       $ readit -quiet

#### How to Install
-----------------

* Clone project from github:
```
  $ git clone https://github.com/ganeshhubale/readit.git
```
* To install package dependencies using pip, run:
```
    $ pip install requests
    $ pip install click
```
* We recommend to create and activate a virtualenv first:
```
	$ cd readit/

  	$ virtualenv -p /usr/bin/python virt

  	$ source virt/bin/activate

  	(virt) $
```
* To install using setup.py file:
```	
	(virt) $ python setup.py install
```
* To make build of project:
```
	(virt) $ python setup.py build
```	

    
 
#### [License](https://github.com/ganeshhubale/readit/blob/master/LICENSE)
----

Readit - Command line tool is licensed under [GNU General Public License v3.0](https://github.com/ganeshhubale/readit/blob/master/LICENSE).



