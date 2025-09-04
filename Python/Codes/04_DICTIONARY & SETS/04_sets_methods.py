a = {1,1,1,2,3,55,2,4,3,2,2}
print(a)

a = {1,1,1,2,3,55,2,4,3,2,2,"Azham"}
print(a,type(a))

a.add(5)
print(a)

s = {1,2,4}
b = {2,3}
print(s-b)
print(s^b)

print(b.issubset(s))
print(s.isdisjoint(b))
print(len(s))