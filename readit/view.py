from beautifultable import BeautifulTable

table = BeautifulTable()
table_tag = BeautifulTable()
table.left_border_char = '|'
table.right_border_char = '|'
table.top_border_char = '='
table.header_separator_char = '='
table.column_headers = ["ID", "URL", "TAG", "DATE", "TIME"]
table_tag.left_border_char = '|'
table_tag.right_border_char = '|'
table_tag.top_border_char = '='
table_tag.header_separator_char = '='
table_tag.column_headers = ["Available TAGs"]


class ShowResults(object):
    """This class includes methods. Which are used to 
        show output to the user in table format.
    """
    def __init__(self):
        pass

    def all_tags(self, tag_list):
        if tag_list:
            for tag_in_list in tag_list:
                table_tag.append_row(tag_in_list)
                print(table_tag)
        else:
            print("Tags are not found in database.")

    def print_bookmarks(self, all_bookmarks):
        if all_bookmarks:
            print("*" * 24, "\nAlready bookmarked URLs.\n", "*" * 23)
            for bookmark in all_bookmarks:
                table.append_row(
                        [bookmark[0], bookmark[1], bookmark[2],
                            bookmark[3], bookmark[4]])
            print(table)
        else:
            print("Bookmarked URLs not available.")
