
import requests  # to check whether url is valid or not
import click  # used for command line interface.
import database as db  # used to perform database operations.


@click.command()
@click.option('--add', '-a', multiple=True, help="Add URLs")
@click.option('--tag', '-t', multiple=True, help="Add URL with tag")
@click.option('--delete', '-d', multiple=True, help="Delete a URL")
@click.option('--clear', '-c', multiple=True, nargs=0, help="Clear bookmarks")
@click.option('--update', '-u', multiple=True, help="Update a URL")
@click.option('--search', '-s', multiple=True, help="Search all URLs by Tag")
@click.option('--view', '-v', multiple=True, nargs=0, help="Show URLs")
@click.argument('insert', nargs=-1, required=False)
def main(insert, add, tag, delete, clear, update, search, view):
    """
    It performs database operations as per arguments passed by user.
    """
    d = db.DatabaseConnection('', '')

    if add:
        for i in add:
            url = i
            try:
                u = requests.get(url)
                r = u.status_code
                if r == 200:
                    d.add_url(url)
                else:
                    print("invalid url:--> ", url)
            except Exception as e:
                print("Exception caught:--> ", e)

    elif delete:
        urlid = []
        for i in delete:
            urlid.append(i)
        for j in urlid:
            d.delete_url(j)

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
                print("invalid url:--> ", url)
        except Exception as e:
            print("exception caught:-->  ", e)

    elif view:
        d.show_url()
    elif search:
        taglist = []
        for i in search:
            taglist.append(i)
        for j in taglist:
            d.search_by_tag(j)
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
            print("Exception Caught:--> ", t)
    else:
        for i in insert:
            url = i
            try:
                u = requests.get(url)
                r = u.status_code
                if r == 200:
                    d.add_url(url)
                else:
                    print("invalid url:--> ", url)
            except Exception as e:
                print("Exception caught:-->  ", e)
