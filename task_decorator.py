# decorator 1
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
print()

#decorator with arugument
def my_decorator(func):
    def wrapper(name):
        print("Before execution")
        func(name)
        print("After execution")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello {name}")

greet("Shubham")
print()

#decoarator 3
def deco1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def deco2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@deco1
@deco2
def test():
    print("Function executed")

test()
