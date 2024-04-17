#1. The Calculator App
#Objective:
#The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

#Task 1: .
#Task 2: Implement user input to receive numbers and an operation choice.
#Task 3: Ensure your program can handle division by zero and other potential errors.

#shopping_list = []


#this works but im getting a weird error after it does the division

def home():

    choice= input("""
A'= 'addition'.
S'  subtraction.
M'  multipliication.
D'  division.
""")
    if choice=='A':
        print('the answer is->>')
    addition(number_1,number_2)
    if choice=='S':
        print('the answer is->>')
    subtraction(number_1,number_2)
    if choice=='M':
        print('the answer is->>')
    multiplication(number_1,number_2)
    if choice=='D':
        print('the answer is->>')
    division(number_1,number_2)

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

#print('{} + {} = '.format(number_1, number_2))
#print(number_1 + number_2)
def addition (number_1 , number_2):
   print (number_1 + number_2)
   return

#print('{} - {} = '.format(number_1, number_2))
#print(number_1 - number_2)
def subtraction (number_1 , number_2):
    print (number_1 - number_2)
    return
#print('{} * {} = '.format(number_1, number_2))
#print(number_1 * number_2)
def multiplication (number_1 , number_2):
    print (number_1 * number_2)
    return

#print('{} / {} = '.format(number_1, number_2))
#print(number_1 / number_2)
def division (number_1 , number_2):
    print (number_1 / number_2)
    return
home()



