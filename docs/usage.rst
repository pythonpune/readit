Usage
=====

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
        -e, --export TEXT...  Export URLs to csv file
        -tl, --taglist TEXT   Show all Tags available in database
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

3. **Update** a bookmark using its ID:

.. code-block:: bash

        $ readit -u url_id url
        or
        $ readit --update url_id url


4. **Delete** a bookmarked URL using its ID:

.. code-block:: bash

        $ readit -d url_id
        or
        $ readit --delete url_id

5. **Clear** all the bookmarks:

.. code-block:: bash

        $ readit -c
        or
        $ readit --clear

6. **Bookmark** URL along with TAG:

.. code-block:: bash

        $ readit -t tag_name url
        or
        $ readit --tag tag_name url


7. **Search** and **Display** all bookmarks using the TAG:

.. code-block:: bash

        $ readit -s tag_name
        or
        $ readit --search tag_name


8. **Open URL** in the Browser using specific ID:

.. code-block:: bash

        $ readit -o urlid
        or
        $ readit --openurl urlid

9. **Export** URLs to CSV file:

.. code-block:: bash

        $ readit -e
        or
        $ readit --export


10. **Show** all Tags available in the database:

.. code-block:: bash

        $ readit -tl
        or
        $ readit --taglist
