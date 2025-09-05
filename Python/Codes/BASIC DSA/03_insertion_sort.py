def insertion (list):
    n = len(list)
    for i in range(1,n):
        key = list[i]
        j = i-1
        while j>=0 and key<list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=key

list = [1,3,5,4,2]
insertion(list)
print(list)