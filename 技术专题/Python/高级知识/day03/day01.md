# 装饰器
就是给已有函数增加额外功能的函数, 它本质上就是一个闭包函数。

装饰器的功能特点：
- 不修改已有函数的源代码
- 不修改已有函数的调用方式
- 给已有函数增加额外的功能

```python
def decorator(func): # 如果闭包函数的参数有且只有一个并且是函数类型, 那么这个闭包函数称为装饰器
    def inner():
        print('已添加登录验证')
        func()
    return inner

def comment():
    print('发表评论')

# 调用方式不变
comment = decorator(comment)
comment()
```

使用语法糖
```python
def decorator(func): # 如果闭包函数的参数有且只有一个并且是函数类型, 那么这个闭包函数称为装饰器
    print('装饰器已执行了')
    def inner():
        print('已添加登录验证')
        func()
    return inner


# 装饰器语法糖的写法：@装饰器名称, 装饰器语法糖就是在装饰以后函数的时候写法更加简单
@decorator  # comment = decorator(comment) 装饰器语法糖对该代码进行了封装 comment = inner
def comment():
    print('发表评论')

# 调用装饰器对已有函数进行装饰
# comment = decorator(comment)

# 调用方式不变
# comment()

# 装饰器的执行时机：当前模块加载完成以后, 装饰器会立即执行, 对已有函数进行装饰
```

装饰器本质就是一个闭包函数, 它可以对已有函数进行额外的功能扩展。
装饰器的语法格式：
```python
def decorator(fn): # fn: 被装饰的目标函数
    def inner():
        '''执行函数之前'''
        fn() # 执行装饰器的目标函数
        '''执行函数之后'''
    return inner
```
装饰器的语法糖用法：@装饰器名称, 同样可以完成对已有函数的装饰操作。




### 装饰器的使用

装饰器的使用场景
1. 函数执行时间的统计
2. 输出日志信息

```python
import time

def get_time(func):
    def inner():
        begin = time.time()
        func()
        end = time.time()
        print('执行时间:', (end - begin))
    return inner

@get_time
def work():
    for i in range(10000):
        print(i)

work()
```


### 通用装饰器
能够写出通用的装饰器


#### 带有参数的装饰器
```python


def decorator(func):
    # 使用装饰器装饰已有函数的时候, 内部函数的类型和要装饰的已有函数的类型保持一致
    def inner(a, b):
        print('正在努力执行加法计算')
        func(a, b)

    return inner

# 用装饰器语法糖方式装饰带有参数的函数
@decorator # add_num = decorator(add_num), add_num = inner
def add_num(num1, num2):
    result = num1 + num2
    print('结果为：', result)

add_num(1, 2)
```

#### 带有参数带有返回值的装饰器
```python

def decorator(func):
    # 使用装饰器装饰已有函数的时候, 内部函数的类型和要装饰的已有函数的类型保持一致
    def inner(a, b):
        print('正在努力执行加法计算')
        return func(a, b)

    return inner

# 用装饰器语法糖方式装饰带有参数的函数
@decorator # add_num = decorator(add_num), add_num = inner
def add_num(num1, num2):
    result = num1 + num2
    return result


result = add_num(1, 2)
print('结果为：', result)
```


#### 带有不定长参数的装饰器

```python


def decorator(func):
    # 使用装饰器装饰已有函数的时候, 内部函数的类型和要装饰的已有函数的类型保持一致
    def inner(*args, **kwargs):
        print('正在努力执行加法计算')
        # *args: 把元组里面的每一个元素, 按照位置参数的方式进行传参
        # **kwargs：把字典里面的每一个键值对, 按照关键字的方式进行传参
        # 这里对元组和字典进行拆包, 仅限于结合不定长参数的函数使用
        return func(*args, **kwargs)

    return inner

# 用装饰器语法糖方式装饰带有参数的函数
@decorator # add_num = decorator(add_num), add_num = inner
def add_num(*args, **kwargs):
    result = 0

    # args: 元组类型
    # kwargs: 字典类型
    for value in args:
        result += value

    for value in kwargs.values():
        result += value

    return result


result = add_num(1, 2)
print('结果为：', result)


```


### 多个装饰器的使用

```python
def mak_div(func):
    print('mak_div装饰器执行了')
    def inner():
        result = "<div>" + func() + "</div>"
        return result
    return inner



def mak_p(func):
    print('mak_p装饰器执行了')
    def inner():
        result = "<p>" + func() + "</p>"
        return result
    return inner

# 多个装饰器的过程, 由内到外的一个装饰过程, 先执行内部的装饰器, 在执行外部的装饰器
# 原理剖析： mak_div(mak_p(content))
# 分步拆解： content = mak_p(content), 内部装饰器装饰完成 content = mak_p.inner
# content =mak_div(mak_p.inner)

@mak_div
@mak_p
def content():
    return 'python'


print(content())

```

### 装饰器带有参数
```python

def return_decorator(flag):

    # 装饰器只能接收一个参数并且是函数类型
    def decorator(func):
        def inner(a, b):
            if flag == '+':
                print('正在努力执行加法计算')
            elif flag == '-':
                print('正在努力执行减法计算')
            func(a, b)
        return inner
    # 当调用函数的时候可以返回一个装饰器decorator
    return decorator

# decorator = return_decorator('+'), @decorator => add_num = decorator(add_num)
@return_decorator('+')
def add_num(a, b):
    result = a + b
    print(result)

@return_decorator('-')
def sub_num(a, b):
    result = a - b
    print(result)

add_num(1, 2)
sub_num(3, 1)

# 带有参数的装饰器, 其实就是定义了一个函数, 让函数接收参数, 在函数内部返回的是一个装饰器
```

使用带有参数的装饰器, 实际上是在装饰器外面又包裹了一个函数, 使用该函数接收参数, 返回的是装饰器, 因为@符号需要配合装饰器实例使用。