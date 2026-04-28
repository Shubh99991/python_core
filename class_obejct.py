class car:

    def hello(self):
        print("Car info")
    name="BMW"
    price=1000000
    color="red"

a=car()
a.hello()
print("name:",a.name)
print("price:",a.price)
print("color:",a.color)

class abc:
    id=0
    name=""

setattr(abc,"id",101)
setattr(abc,"name","python")
print("id",getattr(abc,"id"))
print("name",getattr(abc,"name"))




