list = [1,2,3,4]

n = len(list)
for i in range(n-1):
    for j in range(n-i-1):
     if list[j]>list[j+1]:
        temp = list[j]
        list[j] = list[j+1]
        list[j+1] = temp

print(list)