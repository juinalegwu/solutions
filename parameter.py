def welcome(name):
    print(f"welcome, {name}!")
welcome("Juliet")



def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")
introduce("Juliet", 25)    



def describe_pet(pet, name):
    print(f"My {pet} is called {name}.")
describe_pet("dog", "Bingo")


def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")
introduce(name="Juliet", age=25)    



def add(a, b):
    print(a + b)
add(b=10, a=5)


def greet(name="friend"):
    print(f"Hello, {name}!")

greet("Juliet")


def greet(name="friend"):
    print(f"Hello, {name}!")
greet()
greet("Juliet")



def introduce(name, country="Nigeria"):
    print(f"My name is {name} and I am from {country}")
introduce("Juliet")
introduce("Juliet", "Ghana")



def add(a, b):
    return a + b
result = add(3, 4)
print(result)



def multiply(a, b):
    return a * b
result = multiply(4, 3)
print(result)


def substract(a, b):
    return a - b
result = substract(10, 4)
print(result)

def calculate():
    a = 10
    b = 5
    return a, b
a, b = calculate()
print(a)
print(b)


def introduce():
    name = "Juliet"
    country = "Nigeria"
    return name, country
name, country = introduce()
print(name)
print(country)


def add_numbers(a, b):
    total = a + b
    product = a * b
    return total, product
total, product = add_numbers(20, 5)
 
print(total)
print(product)


def greet(name="friend"):
    print(f"Hello, {name}!")
greet()
greet("Juliet")



def introduce(name, country="Nigeria"):
    print(f"My name is {name} and I am from {country}")
introduce("Juliet")
introduce("Juliet", "Ghana")



def introduce(name, country="Nigeria"):
    return (f"My name is {name} and I am from {country}")
print(introduce("Juliet"))
print(introduce("Juliet", "Ghana"))


def describe_pet(name="Max", pet="dog"):
    return(f"My {pet} is called {name}")
print(describe_pet(name="Max", pet="dog"))


