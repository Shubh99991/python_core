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
