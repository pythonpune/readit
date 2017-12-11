#!/usr/bin/env python
import os
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="An easy to use cli to-do list program.")
    subparser = parser.add_subparsers(help="Commands you can use with the program", 
                                      dest='command')
    
    #subcommand add    
    parser_create = subparser.add_parser('add', 
                                        help="Add a new item to the list.")
    parser_create.add_argument('text', 
                                type=str, 
                                help="Enter the text to be added to the list.")
    parser_create.add_argument('-p',
                                type=str, 
                                choices=['h','m','l'],
                                default="None", 
                                help="Set priority for the item. Options: h=high, m=medium, l=low.")
    parser_create.add_argument('-d',
                                type=str,
                                default="None",
                                help="Set a deadline for the item. Format='2017.12.31'")
    #subcommand list
    parser_list = subparser.add_parser('list', 
                                        help="Show the contents of the list.")
    #subcommand remove
    parser_remove = subparser.add_parser('remove', 
                                        help="Remove an item from the list.")
    parser_remove.add_argument('no', 
                                type=int, 
                                help="Enter the no of the item you want to remove.")
    
    args = parser.parse_args()

    if args.command == 'add':
        add(args.text,args.p,args.d) 
    elif args.command == 'list':
        showlist()
    elif args.command == 'remove':
        remove(args.no)
    else:
        parser.print_help()

def add(add,deadline,priority):
    if not os.path.exists('todo.txt'):
        file = open('todo.txt', 'w+')
    else:
        file = open('todo.txt', 'a+')
    file.write(str(priority) + '"' + str(deadline) + '"' + str(add) + '"' + "\n")
    file.close()
    showlist() 

def showlist():
    W  = '\033[0m'  # white (normal)
    R  = '\033[0;31;1m' # red
    G  = '\033[0;32;1m' # green
    O  = '\033[0;33;1m' # orange
    B  = '\033[0;34;1m' # blue
    P  = '\033[35m' # purple
    try:
        file = open('todo.txt','r+')
    except FileNotFoundError:
        print("Your todo list is empty!\nPlease try adding an item to your list.")
        sys.exit()
    i = 1
    print('{0:<5} \t {1:<20} \t {2:<5}'.format("No:","Task:","Deadline:"))
    for line in file: 
        words = line.split('"')
        if words[1] == 'h':
            print(G +'{0:<5} \t {1:<20} \t {2:<5}'.format(i,  words[2],words[0]) + W)
        elif words[1] == 'm':
            print(O +'{0:<5} \t {1:<20} \t {2:<5}'.format(i,  words[2],words[0]) + W)
        elif words[1] == 'l':
            print(R +'{0:<5} \t {1:<20} \t {2:<5}'.format(i,  words[2],words[0]) + W)
        else:
            print(W +'{0:<5} \t {1:<20} \t {2:<5}'.format(i,  words[2],words[0]) + W)
        i += 1
    file.close()
     
def remove(num):
    file = open('todo.txt','r')
    lines = file.readlines()
    try:
        del lines[num - 1]
    except IndexError:
        print("Line does not exist!")
    else:
        pass
    file.close()
    
    file = open('todo.txt','w')
    for line in lines:
        file.write(line)
    file.close()
    showlist()


main() 
