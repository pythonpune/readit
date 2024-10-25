Usage
=====

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
