#2. The Shopping List Maker
#Objective: The aim of this assignment is to create a program that helps users make a shopping list.

#Task 1: Write a function that lets the user add items to a list until the user replies "stop", and then returns the shopping list. 
#Task 2: Include a feature to remove items from the list. Task 3: Add a feature that prints out the entire list in a formatted way.

shopping_list = []


def show_help():
    print('What should we pick up at the store?')
    print("""
  Enter 'DONE' to stop adding items.
  Enter 'DELETE' to remove item.
  Enter 'SHOW' to see your shopping list.
  """)

def add_to_list(item):
    shopping_list.append(item)
    print('{} was added to your shopping list!'.format(item))#input adding items
    print('You have {} items on your list.'.format(len(shopping_list))) #what items have been inputed too shopping list 

def delete_from_list():

    delete_me = input("Which item would you like to delete from the list? ")
    shopping_list.remove(delete_me)
    print("{} has been removed from the list.".format(delete_me))
        
def show_list():
    print('My Shopping List:')
    for item in shopping_list:
        print(item)

show_list()

show_help()

while True:
    new_item = input('> ')
    if new_item == 'DONE':
        break
    elif new_item == 'DELETE':
        show_list()
        delete_from_list()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
 
    else:
        
    
        add_to_list(new_item)

show_list()