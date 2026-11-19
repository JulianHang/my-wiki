from py01 import user_name

# 函数的参数
在函数定义与调用时, 我们可以根据自己的需求来实现参数的传递。在Python中, 函数的参数一共有两种形式, 形参、实参。

形参：在函数定义时, 所编写的参数就称之为形式参数

实参：在函数调用时, 所传递的参数就称之为实参

```python
def greet(name):
    print(name)

name = '老王'
greet(name)
```
> 注意：虽然我们在函数传递时, 喜欢使用相同的名称作为参数名称, 但是两者的作用范围是不同的。name = '老王', 代表实参, 是一个全局变量。
而greet(name) 函数中的name实际是在函数定义时才声明的变量, 是一个局部变量。


### 函数的参数类型

#### 位置参数

理论上, 在函数定义时, 我们可以为其定义多个参数。但是在函数调用时, 我们也应该传递多个参数，而且正常情况下, 其要一一对应。

```python
def user_info(name, age, address):
    print(f'姓名：{name}, 年龄：{age}, 地址：{address}')
    

user_info('Tome', 29, '美国')
```
> 注意：位置参数强调的是参数传递的位置必须一一对应, 不可颠倒

#### 关键字参数
函数调用, 通过键值形式加以指定

```python
def user_info(name, age, address):
    print(f'姓名：{name}, 年龄：{age}, 地址：{address}')

    
user_info(name = 'Tome', age = 23, address= '美国')

```

#### 函数定义时缺省参数(默认值)
调用函数时可不传该默认参数的值, 注意：所有位置参数必须出现在默认参数前, 包括函数定义与调用, 简单来说, 在定义缺省参数时, 一定要把其写在参数列表的最右侧。

```python
def user_info(name, age, gender = 'male'):
    print(f'姓名：{name}, 年龄：{age}, 性别：{gender}')


user_info('张三', 20)
user_info('王五', 19)
user_info('婉儿', 18, '女')
```

```python
def user_info(name, age, gender = 'male', address = 'a'):
    print(f'姓名：{name}, 年龄：{age}, 性别：{gender}, 地址：{address}')


user_info('张三', 20)
user_info('王五', 19)
# 如果有多个缺省参数的话, 如果有单独传值的话, 那么该值一定会属于第一个缺省参数的值
user_info('婉儿', 18, 'b')
# 如果有多个缺省参数的话, 想要把值传递给其他缺省参数(不是第一个缺省参数), 那么好像只能用关键字参数了
user_info('婉儿', 18, address = 'b')
```


#### 不定长参数

##### 包裹位置参数
不定长参数也叫可变参数， 用于不确定调用的时候会传递多少个参数(不传也可以)的场景。此时, 可用包裹(packing)位置参数, 或者包裹关键字参数, 来进行参数传递, 会更加方便。

```python
def user_info(*args):
    print(args)

user_info('Tom', 20, '美国')
```
注意：传递的所有参数都会被args变量收集, 它会根据传进参数的位置合并为一个元组, args是元组类型。

##### 包裹关键字参数
```python
def user_info(**kwargs):
    print(kwargs)
    print(f'我的名称{kwargs["name"]}')

user_info(name = 'Tom', age = 23, address = '美国')

```
注意：字典类型格式, 对顺序没有要求, 要求key = value 格式

综上：无论是包裹位置参数还是包裹关键字参数, 都是一个组包的过程。
组包：就是把多个数据组成元组或字典的过程。

#### 拆包(元组和字典)

拆包：就是把元组和字典中的数据单独拆分出来, 然后赋予给其他的变量。

##### 元组拆包

```python
def func():
    return 100, 200

num1, num2 = func()
print(f'{num1}, {num2}')
```

##### 字典的拆包过程
字典拆包, 只能把每个元素的key拆出来

```python
dict1 = {'name': 'a', 'age': 18}
a, b = dict1
print(a)
print(b)

print(dict1.get(a))
```

##### 应用案例

案例1：使用至少3种方式交换两个变量的值

```python
c1 = 10
c2 = 2

tmp = c1
c1 = c2
c2 = tmp
print(c1)
print(c2)
```

使用加法和减法运算交换两个变量的值(不需要引入临时变量)
```python
c1 = 10
c2 = 2

c1 = c1 + c2
c2 = c1 - c2
c1 = c1 - c2  # -> c1 + c2 - c1
```

只有Python才具有的特性, 叫做拆包
```python
c1 = 10
c2 = 2
c1, c2 = (c2, c1)
```
原理：
第一步：把c2和c1组成一个元组(c2, c1)
第二步：使用拆包特性, 把元组中的两个元素分别赋值给c1和c2


案例2：数据的传递
```python
def func(*args, **kwargs):
    print(args)
    print(kwargs)

tuple1 = (10, 20, 30)
dict1 = {'first': 40, 'second': 50, 'third': 60}

# *tuple1 会把元组拆成多个位置参数
# **dict1 会把字典拆成多个关键字参数
func(*tuple1, **dict1)

# 如果位置参数跟关键字参数是通过传参的方式的话, 那么通常情况下要加*进行拆包

```

值得注意的是：

```python
dict1 = {'first': 40, 'second': 50, 'third': 60}
print(**dict1) # 会报错, 只能用于函数传参
```