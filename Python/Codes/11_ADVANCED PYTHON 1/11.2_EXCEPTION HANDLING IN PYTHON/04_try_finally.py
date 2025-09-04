'''
In function the try else not work.
'''

def function():
    try:
       a = int(input("Enter the number: "))
       print(a)

    except Exception as a:
        print(a)

    else:
        print("Goodbye")

function()

'''
So, in function we use try finally.
'''

def function():
    try:
       a = int(input("Enter the number: "))
       print(a)

    except Exception as a:
        print(a)

    finally:
        print("Goodbye")

function()