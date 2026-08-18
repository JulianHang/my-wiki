# 子类扩展：重写父类的属性和方法
继承：让子类继承父类的所有公共属性和方法, 但是如果仅仅是为了继承公共属性和方法, 继承就没有实际的意义了, 应该是在继承以后, 子类应该有一些
自己的属性和方法。

> 重写也叫做覆盖, 就是当子类成员与父类成员名字相同的时候, 从父类继承下来的成员会重新定义。此时, 通过子类实例化出来的对象访问相关成员的时候, 真正起作用的是子类中定义的成员。

```python
class Animal(object):
    def eat(self):
        print('i can eat')

    def call(self):
        print('i can call')

class Cat(Animal):
    def call(self):
        print('i can miao miao miao')


class Dog(Animal):
    def call(self):
        print('i can wang wang')


```

思考：重写父类中的call方法以后, 此时父类中的call方法还在吗？

答：还在, 只不过是在其子类中找不到了。类方法的调用顺序, 当我们在子类中重构父类的方法后, Cat子类的实例会先在自己的类Cat中查找该方法, 当找不到
该方法时才会去父类Animal中查找对应的方法。


### 调用父类属性和方法
super：调用父类属性和方法, 完整写法：`super(当前类名, self).属性或方法`, 在python3以后版本中, 调用父类的属性和方法我们只需要使用`super().属性或方法`就可以完成调用。

案例：Car汽车类, GasolineCar汽油车、Electric电动车

```python
class Car(object):
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def run(self):
        print('i can run')

class GasolineCar(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)

    def run(self):
        print('i can run with gasoline')

class ElectricCar(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)
        self.battery = 70

    def run(self):
        print(f'i can with electric remain:{self.battery}')

bwm = GasolineCar('宝马', 'x5', '白色')
bwm.run()

tesla = ElectricCar('特斯拉', 'Model S', '黑色')
tesla.run()

```

### MRO属性或MRO方法
MRO(Method Resolution Order) 方法解析顺序, 我们可以通过`类名.__mro__或类名.mro()`获得`类的层次结构`, 也就是针对同一个方法, 优先调用顺序, 方法解析顺序也是按照这个类的层级结构寻找。

```python
class Car(object):
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def run(self):
        print('i can run')

class GasolineCar(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)

    def run(self):
        print('i can run with gasoline')

class ElectricCar(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)
        self.battery = 70

    def run(self):
        print(f'i can with electric remain:{self.battery}')


print(ElectricCar.mro())
print(ElectricCar.__mro__)

tesla = ElectricCar('特斯拉', 'Model S', '黑色')
tesla.run()

```

说明：由MRO方法解析顺序可知, 在类的继承中, 当某个类创建了一个对象时, 调用属性或方法, 首先在自身类中寻找, 如找到则直接使用, 停止后续的查找。如果未找到, 继续向上一级继承的类中去寻找，
如找到则直接使用, 没有找到则继续向上寻找...直到object类。


```python
class A:
    def show(self):
        print("A")
        super().show()

class B:
    def show(self):
        print("B")
        super().show()

class Base:
    def show(self):
        print("Base")

class C(A, B, Base):
    pass

C().show()
# A
# B
# Base
```
这里 super() 的含义不是固定调用“直接父类”, 而是调用当前类之后、MRO 中的下一个类