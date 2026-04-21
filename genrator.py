def show():
    for i in range(1,11):
        yield i
 
for i in show():
    print(i)
print()

def display():
    s1="hello"
    yield s1

    s2="its monday"
    yield s2

    s3="good bye"
    yield s3

a=display()
print(next(a))
print(next(a))
print(next(a))

#print(display()) it will return object

"""
for i in display():
    print(i)
"""