## 3.插入排序法
lst=[3,5,11,7,6]
n=len(lst)
for i in range(1,n):
    temp=lst[i]
    j = i - 1
    while temp < lst[j] and j>=0:
        lst[j+1]=lst[j]
        j-=1
    lst[j+1]=temp
print(lst)
