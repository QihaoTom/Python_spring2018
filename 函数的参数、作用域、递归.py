##  参数可变or不可变
# 实参不可变
def change(stringB):
    stringB='Hello, python!'
stringA='Hi, Python!'
change(stringA)
print(stringA)

# 实参可变
def change(listB):
    listB=[4,5,6]
listA=[1,2,3]
change(listA)
print(listA)

## 如何获得改变过的形参值
# 用return语句将值返回主调函数使用
def change(stringB):
    stringB='Hello,python!'
    return stringB
stringA='Hi,python!'
print(change(stringA))
print(stringA)

def change(listB):
    listB=[4,5,6]
    return listB
listA=[1,2,3]
print(change(listA))
print(listA)
