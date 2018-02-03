
import requests  # to check whether url is valid or not
import click  # used for command line interface.
import database as db  # used to perform database operations.


@click.command()
@click.option('--add', '-a', nargs=0, help="Add URLs with space-separated")
@click.option('--tag', '-t', nargs=2, help="Add Tag with space-separated URL")
@click.option('--delete', '-d', nargs=1, help="Remove a URL of particular ID")
@click.option('--clear', '-c', multiple=True, nargs=0, help="Clear bookmarks")
@click.option('--update', '-u', nargs=2, help="Update a URL for specific ID")
@click.option('--search', '-s', nargs=1, help="Search all bookmarks by Tag")
@click.option('--view', '-v', multiple=True, nargs=0, help="Show bookmarks")
@click.option('--version', '-V', is_flag=True, help="Check latest version")
@click.argument('insert', nargs=-1, required=False)
def main(insert, add, tag, delete, clear, update, search, view, version):
    """
    Readit - Command-line bookmark manager tool.
    """
    d = db.DatabaseConnection()

    if add:
        for i in add:
            url = i
            try:
                u = requests.get(url)
                r = u.status_code
                if r == 200:
                    d.add_url(url)
                else:
                    print("Invalid URL:--> ", url)
            except Exception as e:
                print("Invalid input:--> ", e)

    elif delete:
        d.delete_url(delete)

    elif update:
        mylist = []
        for i in update:
            mylist.append(i)
        uid = mylist[0]
        url = mylist[1]
        try:
            u = requests.get(url)
            r = u.status_code
            if r == 200:
                d.update_url(uid, url)
            else:
                print("Invalid URL:--> ", url)
        except Exception as e:
            print("Invalid input:-->  ", e)

    elif view:
        d.show_url()
    elif search:
        d.search_by_tag(search)
    elif clear:
        d.delete_all_url()
    elif tag:
        taglist = []
        for i in tag:
            taglist.append(i)
        tag_name = taglist[0]
        tagged_url = taglist[1]
        try:
            u = requests.get(tagged_url)
            r = u.status_code
            if r == 200:
                d.tag_url(tag_name, tagged_url)
            else:
                print("Invalid URL:-->", tagged_url)
        except Exception as t:
            print("Invalid input:--> ", t)
    elif version:
        print("readit 1.0")
    else:
        for i in insert:
            url = i
            try:
                u = requests.get(url)
                r = u.status_code
                if r == 200:
                    d.add_url(url)
                else:
                    print("Invalid URL:--> ", url)
            except Exception as e:
                print("Invalid input:-->  ", e)
