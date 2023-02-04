# This is a basic calculator
# It accepts two numbers and perfom basic arithmetic operations on them

# Author : Ashutosh Ranjan
# Created on : 2023-02-04
# Last modified on : 
# Last modified by : 

# User manual : Just pass what you want to do with the two numbers

def sum(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return (x/y,x%y)

if __name__ == '__main__':
    x = eval(input("Enter 1st number"))
    y = eval(input("Enter 2nd number"))
    choice = input("Choose 1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n")
    if choice == '1':
        print("{} + {} = {}".format(x,y,sum(x,y)))
    elif choice == '2':
        print("{} - {} = {}".format(x,y,sub(x,y)))
    elif choice == '3':
        print("{} * {} = {}".format(x,y,mult(x,y)))
    elif choice == '4':
        Q,R = div(x,y)
        print("{} / {}= {}\n{} % {} = {}".format(x,y,Q,x,y,R))
