cli.py module
=============

It includes various click options.

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


main function
=============

It contains actions taken by click options when user provide arguments along with options to tool.

System modules
==============

1. click
2. requests
