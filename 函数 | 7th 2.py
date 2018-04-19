# 两种方式生成1到100的随机数

## 第一种
import random
random.randint(1,100)

## 第二种
###第二种更好
from random import randint
randint(1,100)

## random模块中常用函数的使用方法
# 从序列中获取一个随机值
random.choice(['C++','Java','Python'])
# 从range（0，10，2）中获取一个随机整数
random.randrange(0,10,2)
#生成（0，1.0）之间的一个随机浮点数
random.random()
# 生成【5，10】之间的一个随机浮点数
random.uniform(5,10)


## 求1——100之间的所有素数
from math import sqrt
def isprime(x):
  if x==1:
    return False
  k=int(sqrt(x))
  for j in range(2,k+1):
    if x%j==0:
      return False
  return True

## 王成军老师的Python基础，使用生成器函数（generator function）
## 生成1-100之间的所有素数！！
def gen_primes(N):
    """Generate primes up to N"""
    primes = set()
    for n in range(2, N):
        if all(n % p > 0 for p in primes):
            primes.add(n)
            yield n

print(*gen_primes(100))


---

# 实现直接可调用，通用性！
## 关键的语句是 if __name__== "__main__": name 和 main前后各有两条下划线
if __name__== "__main__":
  for i in range(2,101):
      if isprime(i):
         print(i,end='')

#p6为包含程序的文件名
p6.isprime(20)

#os包
import os
os.getcwd()
os.chdir(path)

#爬虫
import urllib.request 
f=urllib.request.urlopen('http://www.nju.edu.cn/')
print(f.read(100))
print(f.read(200))
print(f.read(100000))

#
def printStr(x):
    'print the string'
    print(x)

#将一堆数随机打乱
nums=[1,2,3,4,5,6,7]
import random    
random.shuffle(nums)

#计算学生平均成绩
def search(scores):
    maxScore=0
    minScore=100
    for k,v in scores.items():
        aveg=(scores[k][0]+score[k][1]+score[k][2])//3
        if aveg>=maxScore:
            maxScore=aveg
            maxName=k
        if aveg<=minScore:
            minScore=aveg
            minName=k
        return maxName,minName
if __name__=='__main__':
    dictScores={'Jerry':[87,65,91],'Marry':[76,83,88],'Time':[97,95,89],'John':[77,83,81]}
    maxName,minName=search(dictScores)
    print('[0]fot the first place,[1]got the last'.format(maxName,minName))

#lambda好处是，他是一个表达式
def my_add(x,y):return x+y
lambda x,y:x+y
my_add =lambda x,y:x+y
my_add(3,5)

#计算平均成绩
def search(scores):
    t=sorted(scores.items(),key=lambda d:(d[1][0]+d[1][1]+d[1][2])//3) #d为每一项
    return t[len(t)-1][0],t[0][0] #
