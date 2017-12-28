
import argparse
import requests
import database  


if __name__== '__main__':
    """
    This is main funcction.
    It includes atrgparse coding.
    It calls the functions available in database module.

    """

    database_connection = database.DatabaseConnection('','')
   
    # use of argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('default', nargs='*')
    parser.add_argument('-dt','-drop',required=False,  help="delete all bookmarks" ,action="store_true")
    parser.add_argument('-a','-add', nargs='+', help="add bookmarks")
    parser.add_argument('-v','-view',required=False,help="view bookmarks",action="store_true")
    parser.add_argument('-u','-update', nargs=2, help="Update bookmarks by id")
    parser.add_argument('-d','-delete', help="delete bookmarks by id")
    parser.add_argument('-q', '-quiet', help="quiet", action="store_true")
    args = parser.parse_args()
   

    if args.a:
        """

        if This condition is true 
        then it checks whether url is valid or not
        and calls a function - insert_new_record 
        of database module to add url.

        """
        x = len(args.a)
        i = 0
        while i < x:
            urldata = str(args.a[i])
            url = requests.get(urldata)
            if (404==url.status_code):
                print("Invalid URL...")
            else:
                database_connection.insert_new_record(args.a[i])
            i = i + 1
    
    elif args.v:
        """
        If this condition is true then it will call 
        function - query_all  
        of 
        database module and shows the data.

        """
        database_connection.query_all()
    
    elif args.u:
        """

	If this condition is true then it will call 
        function - delete_record 
        of 
        database module and update the data.
	
	"""
        
    
        database_connection.update_record(args.u[0], args.u[1])
    
    elif args.d:
        """

	If this condition is true then it will call 
        function - delete_record  
        of 
        database module and delete the data.
	
	"""

        database_connection.delete_record(args.d)

    elif args.dt:
        """

	If this condition is true 
        then it will call function - drop_table  of 
        database module and drop the table.
	
	"""

        database_connection.drop_table()

    elif args.q:
        """

	If this condition is true 
        then it will call function - query_all  of 
        database module and shows the all data.
	
	"""

        database_connection.query_all()

    elif args.default:
        """

	If this condition is true 
        then it will call function - insert_new_record  of 
        database module to add urls by default.
	
	"""
        j = 0
        y = len(args.default)
        
        while j < y:
            urldata = str(args.default[j])
            url = requests.get(urldata)
            if(404==url.status_code):
                print("invalid URL...")
            else:
                database_connection.insert_new_record(args.default[j])
            j = j + 1
            

    else:
        """
	It helps to novice user.

	"""

        print("-h, --help   show this help message and exit\n",args)
	
    


