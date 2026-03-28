tuple1=(11,22,33,"hello",11)
print(tuple1,type(tuple1))
tuple2=tuple((1,2,3,4))
print(tuple2)
print()

tuple3=("a","c","m","l","e")
print(len(tuple3))
print(tuple2[2])
print(tuple1[-1])
print(tuple1[2:])
print(tuple2[-4:])
print()

tuple4=tuple1+tuple2
print(tuple4)
print(tuple1*2)
print(tuple1.count(11))
print(reversed(tuple3))
print(sorted(tuple3))
print(max(tuple3))
print(min(tuple2))


