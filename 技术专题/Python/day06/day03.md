# 函数

### 定义
函数的定义：
def 函数名(name):
    ...
    函数体代码
    return 返回值

```python
def greet():
    print('您好')

# 调用函数
greet()
```

### return返回值
```python
def return_num():
    # 在函数内部, 当代码执行到return时, 系统会自动认为函数到此执行结束
    return 1
    # 后续代码不会在执行
    return 2

result = return_num()
print(result)
```

如果一个函数要有多个返回值, 该如何书写代码？
答：在Python中, 理论上一个函数只能返回一个结果, 但是如果我们想让一个函数可以同时返回多个结果, 我们可以使用`元组`的形式

```python
def return_num():
    return 1, 2

result = return_num()
print(result)
print(type(result))

```

```python
def size(num1, num2):
    jia = num1 + num2
    jian = num1 - num2
    cheng = num1 * num2
    chu = num1 / num2
    return jia, jian, cheng, chu
```


### 函数的说明文档

```python
def add_student():
    """这是说明文档"""

help(add_student)
```
调用函数的说明文档：help(函数名)

### 封装一个函数

```python
def generate_code(num):
    """generate_code方法主要用于生成指定长度的验证码, 有一个num参数, 需要传递一个int类型的数值"""
    
    pass
```

### 函数的类型注解

> 基本语法
def 函数名(参数) -> 返回值类型:
    ...

```python
def add(a: int, b: int) -> int:
    return a + b
```

### 函数的嵌套

```python
def funcB():
    print('funcB')

def funcA():
    print('funcA')
    funcB()

funcA()
```

嵌套函数的执行流程：
Python代码遵循一个顺序原则，从上往下，从左往右一行一行执行。
当代码执行到第1行时, 则在计算机内存中定义一个funcB函数, 但是其内部的代码并没有真正的执行, 跳过第2行继续向下运行。
...
代码继续往下执行，到第14行, 发现funcA(), 函数体()就代表调用funcA函数并执行其内部的代码。


### 函数的应用

```python
def func(str1: str):
    list1 = str1.split('.')
    list1.reverse()
    return list1

str1 = '1.2.3.4.5'
print(func(str1))
```

### 变量的作用域
在Python中, 定义在函数外部的变量称之为全局变量, 定义在函数内部就称之为局部变量。

全局变量：在整个程序范围内都可以直接使用;
局部变量：在函数的调用过程中, 开始定义, 函数运行过程中生效, 函数执行完毕后, 销毁;

```python
str1 = 'hello'
def func():
    print(f'局部作用域：{str1}')

print(f'全局作用域：{str1}')
func()
```