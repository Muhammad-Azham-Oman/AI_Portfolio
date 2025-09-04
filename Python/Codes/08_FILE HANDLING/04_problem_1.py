f = open("poem.txt","r")
text = f.read()
if ("Twinkle" in text):
    print("Yes")

else:
    print("No")
f.close()