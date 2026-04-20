"""
from modules import *   #one way 
show("yash")
add(9,9)
sub(12,3)
mul(10,10)
div(144,12)
print(person["age"])
"""

"""
import modules;        #second way 
name=input("what is your name?")
modules.show(name)

a=int(input("enter first number:"))
b=int(input("enter second number:"))
modules.add(a,b)
modules.sub(a,b)
modules.mul(a,b)
modules.div(a,b)
"""

import modules as mod
mod.show("yash")
mod.add(9,9)
mod.sub(12,3)
mod.mul(10,10)
mod.div(144,12)

a=mod.person["age"]
print(a)
