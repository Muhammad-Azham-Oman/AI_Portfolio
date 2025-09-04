# Arithmetic operators

a = 6
b = 7
print(a+b)
print(a-b)
print(a*b)
print(a/b)
c = a+b
print(c+b)

# Assignment Operators

a = 9-6 #Assign 9-6 in a
print(a)
b = 7
b += 5 #Increment the value of b by 5 and then assign it to b
print (b)
c = 6+5
c -= 3 #Decrement the value of c by 3 and then assign it to c
print(c)

# Comparison Operators

a = 6 >= 5
print(a)
b = 9 < 6
print(b)
a = 6
b = 6
c = a==b
print(c)
d = a != b
print (d)

# Logical oprators

g = True or False
print(g)

# Logical operators truth tables

# truth table of 'or'
print("True or False is", True or False)
print("True or True is", True or True)
print("False or True is", True or False)
print("False or False is", False or False)

# truth table of 'and'
print("True and False is", True and False)
print("True and True is", True and True)
print("False and True is", True and False)
print("False and False is", False and False)

# truth table of 'not'
print(not(True))
print(not(False))