from importlib import find_loader

# 异常
基本语法：

```python
try:
    可能发生错误的代码
except(捕获):
    如果出现异常执行的代码
```

案例：
```python
try:
    f = open('python.txt', 'r')
except:
    f = open('python.txt', 'w')
    
f.close()
# ... 代码可以继续执行
```

### 捕获指定异常
在以上案例代码中, except相当于捕获了所有异常, 无论遇到什么错误都会自动执行except中封装的代码, 但是有些情况下, 我们想针对性的捕获异常, 并执行相应代码。

基本语法：
```python
try:
    可能遇到异常的代码
except 异常类型:
    捕获到对应的错误以后, 执行的代码
    
```

① 如果尝试执行的代码的异常类型和要捕获的异常类型不一致, 则无法捕获异常。

② 一般try下方只放一些尝试执行的代码

```python
try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
```

### 同时捕获多个异常

```python
try:
    print(name)
    print(10/0)
except(NameError, ZeroDivisionError) as e:
    print(e)
```

### 捕获未知异常
无论我们在except后面定义多少个异常类型, 在实际开发中, 也可能会出现无法捕获的未知异常。这个时候, 我们考虑使用Exception异常类型捕获可能遇到的所有未知异常。

```python
try:
    可能遇到的错误代码
except Exception as e:
    print(e)
```

异常的层级关系
```markdown
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── TypeError
    ├── ValueError
    ├── AttributeError
    ├── NameError
    ├── OSError
    └── RuntimeError
```


### 异常捕获中的else语句
else语句：表示的是如果没有异常要执行的代码。


```python
try:
    可能出现异常的代码
except Exception as e:
    print(e)
else:
    print('没有异常, 正常执行')
```

### 异常捕获中的finally语句
finally表示的是无论是否异常都要执行的代码, 例如关闭文件、关闭数据库连接。
```python
try:
    f = open('python.txt', 'r')
except:
    f = open('python.txt', 'w')
else:
    print('真开心, 正常执行')
finally:
    f.close()
```

### 异常的综合案例

#### 异常的传递

```python
import time

try:
    f = open('python.txt', 'r')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(3)
            print(content, end='')
    except:
        print('python.txt未全部读取完成, 中断了...')
    finally:
        f.close()
except:
    print('python.txt文件未找到')

```

#### raise抛出异常

基本语法
> raise 异常类对象

```python
def input_password():
    password = input('请输入你的密码, 不少于6位')
    if len(password) < 6:
        raise Exception('你的密码长度少于6位')

    print(password)


```

#### 抛出自定义异常类

```python
class ShortInputError(Exception):
    def __init__(self, length, min_length):
        self.length = length
        self.min_length = min_length
    
    def __str__(self):
        return f'您输入的密码长度{self.length}, 不能少于{self.min_length}个字符'


try:
    password = input('请输入你的密码, 不少于6位')
    if len(password) < 6:
        raise ShortInputError(len(password), 6)

except Exception as e:
    print(e)

else:
    print(f'密码输入完整, 你的密码：{password}')
```
