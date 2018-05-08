# 面向对象
# 面向过程（old）、对象、函数式、逻辑式
# 对象：实例，以数据为中心的程序设计方式；类：描述了对象的特征
# 抽象（abstraction）和封装（encapsulation）
# sort方法
# inheriatnce继承，子类（派生类）继承父类（基类），父类保持不变
# class ClassName(object):
    #类文档字符串
    #类体
class Dog:
    'define Dog class'
    def greet(self):
        print('Hi')

# object 可不写
class Dog(object):
    'define Dog class'
    counter=0
    def greet(self):
        print('Hi')
Dog.counter
Dog.greet
x=Dog()
x.greet

# 定义一个实例，在做这个事情
class Dog(object):
    'define Dog class'
    # 类方法的第一个参数总是self，指向实例本身，必须要有的
    def setName(self,name):
        self.name=name
    def greet(self):
        print('Hi')

if __name__=='main':
    dog=Dog()
    # 将name属性赋值,实例化
    dog.setName('Paul')
    print(dog.name)
    
# 子类的定义：单继承，多继承
class Dog(object):
    'define Dog class'
    counter=0
    def __init__(self,name):
        self.name=name
        Dog.counter+=1
    def greet(self):
        print("Hi, I am {:s}, my number is {:d}".format(self.name,Dog.counter))
class BarkingDog(Dog):
    'define subclass BarkingDog'
    def bark(self):
        print('barking')

if __name__=='__main__':
    dog=BarkingDog('Zoe')
    dog.greet()
    dog.bark()

















