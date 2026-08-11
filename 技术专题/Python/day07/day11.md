from py02 import name

# lambda表达式

### 普通函数与匿名函数
如果一个函数有一个返回值, 并且只有一句代码, 可以使用lambda简化

变量 = lambda 函数参数:表达式(函数代码 + return 返回值)

调用方式：变量()

> 注意事项：
lambda 表达式的参数可有可无, 函数的参数在lambda表达式中完全适用; lambda表达式能接收任何数量的参数但只能返回一个表达式的值。

```python
def fn1():
    return 100

print(fn1)  # fn1函数在内存中的地址
print(fn1()) # 代表找到fn1函数的地址并立即执行
```

lambda
```python
fn2 = lambda : 100
print(fn2)
print(fn2())
```

```python
def fn1(num1, num2):
    return num1 + num2

print(fn1(10, 20))

```

lambda
```python
fn2 = lambda num1, num2 : num1 + num2
print(fn2(10, 20))
```

### lambda表达式相关应用


#### 带默认参数的lambda表达式

```python
fn = lambda a, b, c = 10: a + b + c
print(fn(10, 20))
```

#### 不定长参数：可变参数 *args
```python
fn1 = lambda *args:print(args)
print(fn1(10, 20, 30))
```

#### 不定长参数：可变参数 **kwargs
```python
fn2 = lambda **kwargs: kwargs
print(fn2(name = 'Tom', age = 20, address = '美国'))
```

#### 带if判断的labmda表达式
```python
fn = lambda a, b : a if a > b else b
print(fn(10, 20))
```

#### 列表数据 + 字典数据排序
```python
students = [
    {'name':'Tom', 'age': 20},
    {'name': 'Rose', 'age': 19},
    {'name': 'Jack', 'age': 22}
]

# 按name值升序排列
students = students.sort(key = lambda x : x['name'])
print(students)

```