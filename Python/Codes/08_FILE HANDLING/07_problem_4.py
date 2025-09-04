word = "Donkey"
with open("file_problem4.txt") as f:
    content = f.read()
newcontent = content.replace(word,"#####")
    
with open("file_problem4.txt","w") as f:
    f.write(newcontent)