# INHERITANCE 
class User():
    death = "hi"

    def __init__(self):
        print("User has peen created")

    def name(self):
        print("name")

    def eat(self):
        print("eating now!")

class John(User):

    def __init__(self):
        User.__init__(self) # u don't even need this
        print("The user John has been created")

    def imSoCool(self):
        print("YES")

    def eat(self):
        print("I'm new lol") #overrides the original eat func

# the John class can use the functions and elements from original class... does not need to initialize

me = John()
me.name()
me.eat()
print(me.death)

# SPECIAL METHODS

class job():

    def __init__(self, salary, title):
        self.salary = salary
        self.title = title

    def __str__(self) -> str:
        return f"Title: {self.title}, Salary: ${self.salary} and hour"

    def __len__(self):
        return self.salary

janitor = job(1, "jani")
print(janitor) # will print out memory location... needs __str__ func

print(len(janitor)) #returns error
        
# importing modules 
# can simplify the module name to make it easier:

import re as nice

patter = 'hello'
strrrr = 'sometimes i want to say hello to so much people but i say helllo instead and i say hello again and it annoys me'

print(nice.findall(patter, strrrr))

# decorators!

# they are functions that modify how other functions work

def hello():
    return "hello world!"

print(hello())

def func():
    a = 'hello'
    print(locals()) # this will output a DICTIONARY of the local variables

func()

# this will output the global 

print(globals())

# assigning fnctions to new variables

def greet(name='Jonathon'):
    return "greetings "+name

pog = greet

print(pog())

# we can pass functions as arguments

def hello():
    return 'Its jose'

def other(func):
    print('hoi')
    print(func())
    print(type(func))

other(hello)

# decorator T_T :

def new_decorator(func):

    def wrap_func():
        print("code here executes")
        func()
        print('func has been called')

    return wrap_func

def this_needs_decorator():
    print("i need a decorator")

# these two are equivalent:

# this_needs_decorator = new_decorator(this_needs_decorator)
@new_decorator
def this_needs_decorator():
    print("i need a decorator")

this_needs_decorator()