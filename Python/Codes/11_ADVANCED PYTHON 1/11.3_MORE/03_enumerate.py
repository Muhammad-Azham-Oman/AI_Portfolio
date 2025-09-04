a = [23,45,87,43,889]

# index = 0
# for item in a:
#     print(f"The item at {index} is {item}")
#     index += 1

'''
This same thing can be done by using enumerate method
'''

for index , item in enumerate(a):
    print(f"The item at {index} is {item}")