def selection (list):
 n = len(list)
 for i in range(n-1):
    min = i
    for j in range(i+1,n):
        if list[j]<list[min]:
            min = j
            list[i],list[min]=list[min],list[i]
            
list = [20,30,3,2,1]
selection(list)
print(list)