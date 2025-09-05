import random
import string

a = random.choice(string.ascii_uppercase)
print(a,end="")

for i in range(5):
    b = random.choice(string.ascii_lowercase)
    print(b,end="")

c = random.choice(string.punctuation)
d = random.choice(string.digits)

print(c,end="")
print(d,end="")