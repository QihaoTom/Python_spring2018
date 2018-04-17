## 3.插入排序法
lst=[3,5,11,7,6]
n=len(lst)
# 当i=3，j=2
for i in range(1,n):
    temp=lst[i]
    j = i - 1
    while temp < lst[j] and j>=0:
        #11往后挪，变为3，5，11，11，6
        lst[j+1]=lst[j]
        j-=1
        #j=1
    lst[j+1]=temp
        #把7赋回去，变为3，5，7，11，6
print(lst)


