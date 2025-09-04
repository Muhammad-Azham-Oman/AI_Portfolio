## Read file

f = open("file.txt","r")
text = f.read()
print(text)
f.close()


## Read line

f = open("file.txt","r")
line = f.readline()
print(line)
f.close()


## Read lines

f = open("file.txt","r")
line = f.readlines()
print(line)
f.close()