# 魔术方法
在python中, `__xx__()`的函数叫做魔法方法, 指的是具有特殊功能的函数。

### __init__() 方法(初始化方法或构造方法)

__init__方法作用：实例化对象时, 连带其中的参数, 会一并传给init函数并执行它。init函数的参数列表会在开头多出一项, 它永远指代新建的那个实例对象, python语法要求这个参数必须要有, 名称为`self`

```python
class Person():
    def __init__(self, name, age):
        # 赋予name属性、age属性给实例化对象本身
        # self.实例化对象属性 = 参数
        self.name = name
        self.age = age

p1 = Person('Tom', 19)

```

> ① __init__方法, 在创建一个对象时默认被调用, 不需要手动调用; ② __init__(self) 中的self参数, 不需要开发者传递, python解释器会自动把当前的对象引用传递过去。


### __str__()方法
当使用print输出对象的时候, 默认打印对象的内存地址, 如果类定义了`__str__`方法, 那么就会打印从这个方法return回去的内容。

```python
class Car():
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        
    # 信息输出
    def __str__(self):
        return f'汽车品牌:{self.brand}'

c1 = Car('奔驰', 'S600', '黑色')
print(c1)

```

> ① __str__方法是在类的外部, 使用print对象时, 自动被调用; ② 在类的内部定义__str__方法, 必须使用`return`返回一个字符串数据


### __del__()方法(删除方法或析构)
当删除对象时, python解释器会默认调用 __del__方法

```python
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __del__(self):
        print(f'{self}对象已经被删除')


p1 = Person('tom', 20)
del p1
```

使用场景： 主要用于关闭文件操作、关闭数据库连接等等。

### 总结

