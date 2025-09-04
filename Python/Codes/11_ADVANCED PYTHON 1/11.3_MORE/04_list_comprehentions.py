a = [1,2,3,4,5,6]

# sq_a = []
# item = 0
# for item in a:
#     sq_a.append(item*item)
#     item+=1
# print(sq_a)

'''
Same thing can be done by:...
'''

sq = (i*i for i in a)
print(list(sq))