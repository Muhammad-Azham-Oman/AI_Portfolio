a = 43

def function():
    global a
    a = 35
    print(a)

function()
print(a)