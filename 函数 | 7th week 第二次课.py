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


# 实现直接可调用，通用性！
## 关键的语句是 if __name__== "__main__": name 和 main前后各有两条下划线
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


if __name__== "__main__":
  for i in range(2,101):
      if isprime(i):
         print(i,end='')
