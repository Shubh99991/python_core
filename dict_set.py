dict1={"name":"abc","roll_no":101,"n":"pqr","r":102}
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1["name"])
print(dict1.get("roll_no"))
d=dict1.copy()
print(d)
print(dict1.items())
d.popitem()
print(d)
dict1.update({".e":"lmn"})
print(dict1)
print()


set1={1,2,3,4,6,2}
print(set1)
set1.add(9)
print(set1)
set1.remove(2)
print(set1)
set2={65,43,2,3,1,2}
set3={54,3}
set1.intersection_update(set2,set3)
print(set1)
a=set1.union(set2)
b=set1.intersection(set2)
print(a)
print(b)
set1.pop()#random deletion
set2.discard(43)#specific deletion
print(set1)
print(set2)
set1.update(set2)
print(set1)
