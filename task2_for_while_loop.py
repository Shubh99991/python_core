#for loop 10 questions and 8 while loop
#element retriving using loop
#string
"""
s="shubham"
for i in s:
    print(i)
print()

a="shubham"
i=0
while(i<len(a)):
    print(a[i])
    i+=1
print()

#element present in string or not
a=input("enter your finding:")
for j in range(0,len(s)):
    if(s[j]==a):
        print(a,"present in",j)
        break
    else:
        print("not present")
        break
print()
j=0
while(j<len(s)):
    if(s[j]==a):
        print(a,"present in",j)
        break
    j+=1
else:
    print("not present")

"""
#list
"""
list=[1,2,3,4,5,6]
for i in list:
    print(i)
print()

#addition of list element
count=0
for i in range(0,len(list)):
    count+=list[i]
print(count)
print()

i=0
sum=0
while(i<len(list)):
    sum+=list[i]
    i+=1
print(sum)
"""
#sum of number and factorial of number
"""
a=int(input("enter number:"))
sum=0
for i in range(1,a+1):
    sum+=i
print(sum)
print()

mul=1
for i in range(1,a+1):
    mul*=i
print(mul)
print()

sum=0
i=1
while(i<=a):
    sum+=i
    i+=1
print(sum)
print()

mul=1
i=1
while i<=a:
    mul*=i
    i+=1
print(mul)
print()


"""
#palindrome or not
"""
a=int(input("enter a number to check wether it is palindrome of not:"))
rev=0
n=a

while(a>0):
    dig=a%10
    rev=rev*10+dig
    a//=10
print(rev)

if(n==rev):
    print("its a palindrome")
else:
    print("not a palindrome")

"""
#table of number
"""
a=int(input())
i=1
while i<11:
    print(a,"X",i,"=",a*i)
    i+=1
print()

for j in range(1,11):
    print(a,"X",j,"=",a*j)

"""
#square pattern
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
print()
"""
#linear search
list=[1,2,3,4,6,7,8]
n=int(input("enter searching number:"))
for i in range(0,len(list)):
    if(n==list[i]):
            print(n,"is found at index",i)
            break;
else:
    print("not found")
print()
"""

#binary search
list=[12,24,36,48,60,72,84,96,108,120]
print(list)
n=int(input("enter searching number:"))
beg=0
end=len(list)-1
while(beg<end):
    mid=(beg+end)/2
    a=int(mid)
    if(n==list[a]):
        print(n,"at index",a)
        break
    elif(list[a]<n):
        start=mid+1
    else:
        end=mid-1
else:
    print("not found")


    















































    
    
