# 面向对象的三大特性
封装、继承、多态

> 封装：将属性和方法书写到类的里面的操作即为封装, 封装可以为属性和方法添加私有权限

> 继承：子类默认继承父类的所有属性和方法, 与此同时子类也可以重写父类属性和方法

> 多态：多态是同一类事物具有的多种形态, 不同的对象调用同一个接口(方法), 表现出不同的状态, 称为多态


### 私有属性

设置私有属性和私有方法很简单, 在属性名和方法名前面加上两个下划线 `__` 即可。

基本语法：

```python
class Girl():
    def __init__(self, name):
        self.name = name
        self.__age = 18


xiaomei = Girl('小美')
print(xiaomei.name)
print(xiaomei.__age)   # 报错

```
> 类中的私有属性和私有方法, 不能被其子类继承。

由以上代码运行可知, 私有属性不能在类的外部被直接访问, 但是出于种种原因, 我们想在外部对私有属性进行访问, 该如何访问？
答：可以定义一个统计的访问接口(函数), 专门用于实现私有属性的访问。

#### 私有属性设置与访问接口
在python中, 一般定义函数名`get_xx`用来获取私有属性, 定义`set__xx`用来修改私有属性值

```python
class Girl():
    def __init__(self, name):
        self.name =  name
        self.__age = 19

    def get__age(self):
        return self.__age
    
    
    def set__age(self, age):
        self.__age = age


girl = Girl('x')
girl.set__age(20)
print(girl.get__age())
```


### 私有方法

私有方法的定义方式与私有属性基本一致, 在方法名的前面添加两个下划线 `__方法名()`

