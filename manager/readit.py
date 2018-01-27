import requests  # to check whether url is valid or not
import click  # used for command line interface.
import database as db  # used to perform database operations.


@click.command()
@click.option('--add', '-a', multiple=True, help="Add URLs")
@click.option('--delete', '-d', multiple=True, help="Delete a URL")
@click.option('--clear', '-c', multiple=True, nargs=0, help="Clear database")
@click.option('--update', '-u', multiple=True,  help="Update a URL")
@click.option('--view', '-v', multiple=True, nargs=0,  help="Show URLs")
@click.argument('insert', nargs=-1, required=False)
def main(insert, add, delete, clear, update, view):
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
    elif clear:
        d.delete_all_url()
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
