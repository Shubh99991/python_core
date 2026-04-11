import os
f=open("demo.txt","r")
#print(f.read())
#print(f.read(5))
#print(f.readlines())
for i in f:
    print(i)

#adding new file with content

f1=open("demo.txt","w") #w mode add the element 
f1=open("demo.txt","a") #a is used to append data in line
f1.write("this is april")
f1=open("demo.txt","r")
print(f1.read())


#f1=open("demo3.txt","x") #x mode is used to creat empty file
#os.remove("demo3.txt")  #it will remove the file

#check whether file is deleted or not 
#if os.path.exists("demo3.txt"):
#    os.remove("demo3.txt")
#else:
#    print("file already deleted")

#with staement is used to oepn and close file without corrupting the  file content

with open("demo4.txt","w") as f:
    content=f.write("hello")
    print(content)
