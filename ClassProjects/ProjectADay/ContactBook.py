import time


#Simple program that takes inputs and addes them to an address book
print("Welcome to the adress book. Please type 'Help' for a list of commands")
'''
List of commands that need made:
    Adding item to address book
    Deleting item from address book
    Editing item in address book
    List all contacts
    Seek contact list
    Search by field


List of functions that are non-command oriented:
    Create a function to parse inputs and clean them up if not good for required field
    save function to acces and manage contacts in seperate .json file.

'''
def help():
    print("Here is a list of all the commands and their functions")
    return True



print("Starting up contact book\n. . .")
print("Type HELP for a list of commands")
while True:
    command = input(">> ")
    if command.lower() == "help":
        helpComm()
    elif
