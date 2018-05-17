# 防止直接报错，加入try和多个except，来允许犯错
try:
    num1=int(input('Enter the first number:'))
    num2=int(input('Enter the second number:'))
    print(num1/num2)
except ValueError:
    print('Please input a digital')
except ZeroDivisionError:
    print('The second number cannot be zero!')
else:
    print('Aha, I am smart.')
  
#  第二种写法
try:
    num1=int(input('Enter the first number:'))
    num2=int(input('Enter the second number:'))
    print(num1/num2)
except(ValueError,ZeroDivisionError):
    print('invalid input')
else:
    print('Aha, I am smart.')
    
#加入while True实现多次输入，并else：break终止循环
while True:
    try:
        num1=int(input('Enter the first number:'))
        num2=int(input('Enter the second number:'))
        print(num1/num2)
    except ValueError:
        print('Please input a digital')
    except ZeroDivisionError:
        print('The second number cannot be zero!')
    else:
        break

# 做一个输出：给一个i，使之+1，再+1，达到5，退出
aList=[1,2,3,4,5]
i=0
while True:
    try:
        print(aList[i])
    except IndexError:
        print('index error')
        break
    else:
        i+=1

# finally 子句
def finallyTest():
    try:
        x=int(input('Enter the first number:'))
        y=int(input('Enter the second number:'))
        print(x/y)
        return 1
    except Exception as err:
        print(err)
        return 0
    finally:
        print('it is a finally clause.')
result=finallyTest()
print(result)
               
# Context Manager
## 定义一个初始数字
c=0
with open('companies.txt') as f:
    for line in f:
        print(line)
        c+=1
        print(c)

#       
try:
    f=open('data.txt')
    for line in f:
        print(line,end='')
except IOError:
    print('Cannot open the file!')
finally:
    f.close()
    
        
        
        
        
        
        
        