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

# 修改形参对实参的影响,实参也跟着变
def change(listB):
    listB[0]=88
    return listB
listA=[1,2,3]
print(change(listA))
print(listA)

# 修改形参的值不影响实参的做法
def change(listB):
    listB[0]=88
    return listB
listA=[1,2,3]
# 不能用“backup_listA=listA”语句
backup_listA=listA[:]
print(change(listA))
print(listA)
print(backup_listA)

## 1.位置参数
def printGrade(name,stuID,grade):
    print("{0}({1})'s grade is {2}".format(name,stuID,grade))
printGrade('Mary','1002','A')
# 错误的结果
printGrade('A','1002','Mary')

## 默认参数,定义默认参数必须放在非默认参数的后面
def printGrade(name,grade,className='Courage'):
    print("{0}{1}'s grade is {2}".format(name,className,grade))
printGrade('Mary','A')

## 3.默认参数的值可以改变
def f(x,y=True):
    'x and y both correct words or not'
    if y:
        print(x,'and y both correct')
    print(x,'is OK')
f(68)
f(68,False)

## 4.可变长参数
def greeting(args1,*tupleArgs):
    print(args1)
    print(tupleArgs)
greeting('Hello','NJU','PKU','THU')

## 可变长参数——可变长位置参数和可变长关键词参数
def greeting(args1,*tupleArgs,**dictArgs):
    print(args1)
    print(tupleArgs)
    print(dictArgs)
names=['NJU','PKU','THU']
info={'schoolName':'NJU','City':'Nanjing'}
greeting('Hello,',*names,**info)
