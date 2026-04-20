#exception means unexpected error which disrupts the flow of excution
a=int(input("enter a number:"))
b=int(input("enter 2 number:"))

"""
try:
    c=a/b
    print(c)
except:
    print("invalid output")
"""
#if we know the error name
try:
    c=a/b
    print(c)
except ZeroDivisionError as z:
    print(z)

#raise
try:
    if(a<=18):
        raise ValueError("there is a value error")
    else:
        print("you are eligible for voting")

except ValueError as v:
    print(v)