#list
list1=list([1,2,3,4,5])
print(list1)
print(type(list1))

#concatenation and multiplication
list2=[4,6,7,8,9]
list3=list1+list2
print(list3)
print(list2*2)
print()

#indexing
print(list1[1])
print(list1[-4])

#slicing
print(list1[2:])
print(list1[-5:-1])
print()

#list methods
sub=["web","python","c","sql"]
sub2=["dsa","math"]
sub[0]="java"
sub.insert(0,"web")
sub.append("r lang")
print(sub)
sub.append(sub2)
print(sub)
sub2.clear()
print(sub2)
sub3=sub.copy()
print(sub3)
print()

print(list3.count(4))
print(list3.index(4))
print(sub.index("python"))
sub.insert(2,"ml")
sub.pop(-1)
print(sub)
sub.pop() #it will pop last element in the list
print(sub)
s=sub.pop() #it will give poped element
print(sub)
print(s)
print()

sub.reverse()
print(sub)
a=[4,8,2,9,1,80]
a.sort()
print(a)
a.sort(reverse=True) #descending order
print(a)
print()

l=["w","a","o","e"]
l.sort()
print(l)
l.sort(reverse=True)
print(l)
print()



































