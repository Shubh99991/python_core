#default function
def hello():
    print("hello")
hello()

#parameterized function
#required parameter(if thier is two parameters then we have put two arguments in calling)
def power(a,b):
    print(a**b)
power(2,3)

#keyword arugement(inside function we can use keywords)
def python(name,age,city):
    print("my name is",name,",im",age,"years old.living in",city)
    print()

python(city="solapur",name="yash",age=21)

#default argument
def python(name,city="pune"):
    print("my name is",name,"living in",city)
    print()

python(name="yash",city="solpaur")
python(name="om")

#variable length argument *arg and **keyword args
def react(name,*marks):
    print(name)
    print(marks)
    print()
    
react("abc",3,4,5,6,7,3)

def react(name,**marks):
    print(name)
    print(marks)
    print()
    
react("abc",a=3,b=4,c=5,d=6,e=7,f=3)

#return statement(it is used to access local variable inside the function)
def add1(a,b):
    result=a+b
    return result

print(add1(44,66))

def number(n):
    if n==0:
        return 1
    else:
        return n * number(n-1)
print(number(5))

#lambda function
#even or odd
even_odd=lambda n:n%2==0
total=even_odd(4)
print(total)

#sum of two number using lambda function
sum1=lambda n1,n2:n1+n2
total=sum1(34,46)
print(total)

#squre
squ=lambda n:n*n
total=squ(5)
print(total)

#divisible by 5
div=lambda n:n%5==0
total=div(90)
print(total)

#list method where lambda function is used
list1=[2,3,4,5,6,7]
newlist1=list(filter(lambda n:n%2==0,list1)) #filter method in list used to filter out desired element from list 
print(newlist1)

newlist2=list(map(lambda n1:n1*n1,list1))#map method in list used to target easch element in list 
print(newlist2)

#recusrion concept in python 
#factorial using recursion
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return (n*fact(n-1))

n=int(input("enter a number:"))
print(fact(n))

#sum of n number using recursion
def sum(n):
    if n==0 or n==1:
        return 1
    else:
        return (n+sum(n-1))
    
n=int(input("enter a number:"))
print(sum(n))





























