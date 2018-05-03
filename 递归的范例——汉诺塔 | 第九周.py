# 实现递归的范例————汉诺塔
## 如何理解呢：以3个为例，要实现的无非就是，把n-1个从A到B，以及B到C，而当n==1时，是A到C
## 所以代码里，即为当n==1时，把A到C，除了这个情况以外，都是A（通过C）到B，同理，B（通过A）
## 到C
def hanoi(a,b,c,n):
    if n==1:
        print(a,'-->',c)
    else:
        hanoi(a,c,b,n-1)
        print(a,'-->',c)
        hanoi(b,a,c,n-1)
n=int(input('input the number of plates:'))
hanoi('a','b','c',n)
        
