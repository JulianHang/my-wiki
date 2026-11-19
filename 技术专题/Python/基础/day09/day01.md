# python中的继承

基本语法
```python
class B(object):
    pass

class A(B):
    pass

```

> 在python中, 所有类默认继承object类, object类是顶级类或基类, 其他子类叫派生类

```python
class Person(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def eat(self):
        print('i can eat food')

    def speak(self):
        print('i can speak')

class Teacher(Person):
    pass

# 内部会调用父类的__init__方法
teacher = Teacher('tom', 20, '美国')
teacher.speak()

```

### 继承相关的几个概念

继承：一个类从另一个已有的类获取其成员的相关特性

派生：从一个已有的类产生一个新的类

单继承：一个类只能继承自一个其他的类, 不能继承多个类, 单继承也是大多数面向对象语言的特性

多继承：一个类同时继承了多个父类


#### 单继承

```python
class Person(object):
    pass

class Teacher(Person):
    pass


```

传递性：A继承B、B继承C, 那么A会继承B、C类中的所有属性和方法(公共)

```python
class C(object):
    def func(self):
        print('我是C类中的相关方法func')

class B(C):
    pass

class A(B):
    pass

a = A()
a.func()

```

#### 多继承

```python
class B(object):
    pass

class A(object):
    pass

class C(A, B):
    pass

```

案例：汽油车、电动车=》混合动力汽车

```python
class GasolineCar(object):
    
    def run_with_gasoline(self):
        print('i can run with gasoline')

class ElectricCar(object):
    
    def run_with_electric(self):
        print('i can run with electric')


class HybridCar(GasolineCar, ElectricCar):
    pass

tesla = HybridCar()
tesla.run_with_electric()
tesla.run_with_gasoline()

```

> 虽然多继承允许我们使用同时继承多个类, 但是在实际开发中, 应尽量避免使用多继承, 因为如果两个类中出现了相同的属性和方法会产生命名冲突