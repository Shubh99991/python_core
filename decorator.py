"""
def display(text):
    print(text)
display("hi")
show=display
show("hello")

"""
def display(func):
    def inner():
        print("i am inner function")
        func()
    return inner

@display # @ uesd as decorator
def show():
    print("i am outer function")
show()
print()


def show1():
    print("we are in first function")

    def func1():
        print("this is first child function")
    def func2():
        print("this is second child function")

    func1()
    func2()

show1()