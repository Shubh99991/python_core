#default function
def hello():
    print("this my default function")

hello()

#calculator
def add1(a,b):
    result=a+b
    return result

def sub1(a,b):
    result=a-b
    return result

def mul1(a,b):
    result=a*b
    return result

def div1(a,b):
    result=a/b
    return result

print("1 for add")
print("2 for sub")
print("3 for mul")
print("4 for div")
print("5 for exit")
a=int(input("enter a number:"))
b=int(input("enter second number:"))
n=int(input("enter choice:"))

if(n==1):
    print(add1(a,b))
elif(n==2):
    print(sub1(a,b))
elif(n==3):
    print(mul1(a,b))
elif(n==4):
    print(div1(a,b))
else:
    exit
print()

def check_even_odd(n):
    return "even" if n%2==0 else "odd"
d=int(input("enter a number:"))
print(check_even_odd(d))
print()

def max_num(a,b):
    return a if a>b else b
a=int(input("enter a number:"))
b=int(input("enter second number:"))
print(max_num(a,b))
print()

def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
print("factorial of 4 is:",factorial(4))
print()

def sum(n):
    result=0
    for i in range(1,n+1):
        result+=i
    return result
print("sum of 4 is:",sum(4))
print()


def area_circle(r,pi=3.14):
    return r*r*pi
print("area of circle:",area_circle(5))





