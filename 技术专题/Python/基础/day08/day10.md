# 类
在python中, 我们可以有两种类的定义方式：

① python2 经典类

不由任意内置类型派生出的类
```python
class 类名:
    # 属性
    # 方法
```

② python3 新式类
```python
class 类名():
    # 属性
    # 方法
```

类名不区分大小写, 遵守一般的标识符的命名规则, 一般为了和方法名相区分, 类名的首字母一般大写


```python
class Person():

    # 方法(函数)
    def eat(self):
        print('我喜欢吃零食')

    def drink(self):
        print('我喜欢喝可乐')

```


### 类的实例化

基本语法
> 对象名 = 类名()

案例：把Person类实例化为对象p1

```python
class Person():
    def eat(self):
        print('我喜欢吃零食')

    def drink(self):
        print('我喜欢喝水可乐')


p1 = Person()
p1.eat()
p1.drink()
```

### self关键字
self也是python内置的关键字之一, 其指向了类实例本身。一句话总结：类中的self就是谁实例化了对象, 就指向谁

```python
class Person():
    def speak(self):
        print(self)
        print('Nice to meet you')

p1 = Person()
p1.speak()
```


### 对象属性
基本语法

> 对象名.属性 = 属性值

案例：
```python
class Person():
    pass


p1 = Person()
p1.name = '老王'
p1.age = 18
p1.address = '美国'

print(f'我的姓名：{p1.name}')
```

### 在类的内部获取外部定义的属性

```python
class Person():
    def speak(self):
        print(f'我的名称：{self.name}')


p1 = Person()
p1.name = '孙悟空'
p1.speak()
```
目前我们的确可以通过`对象.属性`的方式设置或获取对象的属性, 但是这种设置属性的方式有点繁琐, 每次定义一个对象, 就必须手工设置属性。


