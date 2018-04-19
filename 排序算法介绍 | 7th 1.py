## 排序算法三种方法介绍

## 1.选择排序法
lst=[3,5,11,7,6]
n=len(lst)
    #n=5,i=0
for i in range(n-1):
    #point相当于一个指针
    point=i
    #j=0
    for j in range(i+1,n):
        if lst[point]>lst[j]:
            #比完后，放最小值的索引
            point=j
    if point !=i:
        lst[i],lst[point]=lst[point],lst[i]
print(lst)

## 2.冒泡法排序
lst=[3,5,11,7,6]
n=len(lst)
#大循环
for i in range(n-1):
    #加入开关，True和1等价，Flase和0等价
    Flag=1
    for j in range(n-1-i):
        #相邻的两个
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
            #产生一次交换，这里与0不一样的数值即可
            flag=0
        if flag:
            break
print(lst)

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


