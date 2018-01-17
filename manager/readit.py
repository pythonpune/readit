import click
import database

@click.command()
@click.option('--add','-a', multiple=True, help="add")
@click.option('--delete','-d', multiple=True, default='', help='delete')
@click.option('--update','-u', multiple=True, nargs=2, default='', help='update')
@click.option('--show','-s', multiple=True, nargs=0,  help='show')

@click.argument('insert', nargs=-1, required=False)


def main(insert, add, delete, update, show):
    
    d = db.DatabaseConnection('', '')
    
    if add:
        for i in add:
            url = i
            d.add_url(url)
   
    elif delete:

        click.echo("delete: {0}".format(delete))
        for i in delete:
            urlid = i
            d.delete_url(urlid)
            print(urlid)
   
    elif update:
        mylist = []
        click.echo("update {0}".format(update))
        for i in update:
            mylist.append(i)
           # d.update_url(i)
        print(mylist)
    
    elif show:
        
        click.echo("show: hello")
        d.show_url()
    
    else:
        
        for n in insert:
            click.echo("hello: %s" %(n))
            d.add_url(n)

    
