#if else,else if,ladder if,nested if
#age driving
"""
a=int(input("enter a age:"))
if(a>=18 and a<=100):
    print("you are eligible for driving")
else:
    print("not eligible for the driving")
"""
#weekfinder
"""
a=int(input("enter number between 1 to 7:"))
if(a==1):
    print("monday")
elif(a==2):
    print("tuesday")
elif(a==3):
    print("wednesday")
elif(a==4):
    print("thursday")
elif(a==5):
    print("friday")
elif(a==6):
    print("saturday")
elif(a==7):
    print("sunday")
else:
    print("invalid")
"""
#group classifier
"""
a=int(input("enter your age:"))
if a>0 and a<=12:
    print("you are child")
elif(a>13 and a<=19):
    print("you are teen")
elif(a>20 and a<=64):
    print("you are adult")
elif(a>65 and a<=100):
    print("you are senior")
else:
    print("invalid age")
"""
#discount calculator
"""
a=int(input("enter your total shopping amount:"))
if(a>=1000):
    i=a*(10/100)
    print(a-i,"it's your amount after discount")
elif(a>=3000 and a<=5000):
    i=a*(25/100)
    print(a-i,"it's your amount after discount")
elif(a>5000 and a<=10000):
    i=a*(50/100)
    print(a-i,"it's your amount after discount")
else:
    print("not eligible for discount")
"""
#month finder
"""
a=int(input("enter number between 1 to 12:"))
if(a==1):
    print("january")
elif(a==2):
    print("february")
elif(a==3):
    print("march")
elif(a==4):
    print("april")
elif(a==5):
    print("may")
elif(a==6):
    print("june")
elif(a==7):
    print("july")
elif(a==8):
    print("august")
elif(a==9):
    print("september")
elif(a==10):
    print("october")
elif(a==11):
    print("novemeber")
elif(a==12):
    print("december")
else:
    print("invalid")
"""
#login validation
"""
a="shubhs"
b=1601
c=input("enter username:")
d=int(input("enter a password:"))
if(a==c):
    print("user name is correct")
    if(d==b):
        print("password is correct")
        print("successfully login")
    else:
        print("password is incorrect")
else:
    print("invalid user name and password")
"""
#scholarship eligibility

a=int(input("enter cgpa:"))
b=int(input("enter a income:"))
if(a>=7.5):
    print("your marks are eligible")
    if(b<=100000):
        print("yous income matches")
        print("you are eligible for scholaship")
    else:
        print("yous income is not matches")
        print("you are not eligible for scholarship")
else:
    print("not eligible")





























