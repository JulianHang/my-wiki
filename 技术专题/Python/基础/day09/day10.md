# 面向对象其他特性

### 类属性
python中, 属性可以分为实例属性和类属性。类属性就是类对象中定义的属性, 它被该类的所有实例对象所共有, 通常用来记录与这类相关的特征, 类属性不会用于记录具体对象的特征。

```python
class Person(object):
    # 定义类属性
    count = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Tom', 10)
p2 = Person('Som', 20)
```

> 类属性在内存中是一个特殊的存在, 其不同于以前讲过的局部变量(局部变量当函数执行完毕后, 其会被内存苏哦销毁)。但是类属性一旦定义, 除非对象以及这个类在内存中被销毁了, 否则其不会自动销毁。

### 类属性操作
定义count类属性, 用于记录实例化Person类, 产生对象的数量。

```python
class Person(object):
    # 定义类属性
    count = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count = Person.count + 1

p1 = Person('Tom', 10)
p2 = Person('Som', 20)
print(f'创建了{Person.count}个实例对象')
```

### 类方法
类方法就是针对类对象定义的方法, 在类方法中可以直接访问类属性或者调用其他类方法。

```python
@classmethod
def 类名称(cls):
    pass
```
类方法需要用修饰器`@classmethod`来标识, 告诉解释器这是一个类方法, 类方法的第一个参数应该是`cls`

① 哪一个类调用的方法, 方法内的cls就是哪一个类的引用

② 这个参数和示例方法的第一个参数跟`self`类似

③ 使用其他名称也可以, 不过习惯使用`cls`, 通过类名.调用类方法, 调用方法时, 不需要传递cls
参数

④ 在方法内部可以通过cls访问类的属性， 也可以通过cls调用其他的类方法

```python
class Tool(object):
    # 类属性
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod
    def get_count(cls):
        print(f'我们使用Tool类实例化{cls.count}')


t1 = Tool('铁锹')
Tool.get_count()
```

### 静态方法
在开发时, 如果需要在类中封装一个方法, 这个方法：

① 既不需要访问实例属性或者调用实例方法

② 也不需要访问类属性或者调用类方法

这个时候, 可以把这个方法封装成一个静态方法

```python
@staticmethod
def 静态方法名():
    pass
```

```python
class Game(object):
    
    @staticmethod
    def menu():
        print('1、开始游戏')

Game.menu()
```