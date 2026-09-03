# 函数签名
python有些底层代码看不到真实的函数签名, 因为底层是C语言实现, 此时可以使用 help 方法来查看真实入参和出参

```python

# 在函数签名中，/ 和 * 是参数分隔符
# / 左边的参数只能使用位置参数
# * 右边的参数只能使用关键词参数
# / 和 * 中间的参数既可以使用位置参数，也可以使用关键词参数

def func(a, b, /, c, *, d, e):
    pass

func(1, 2, 3, d=4, e=5)
func(1, 2, c=3, d=4, e=5)
```

# 拆包
```python
name, age = 't', 20

first, *middle, last = [1, 2, 3, 4, 5]

print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

# is用法

is  比身份：是不是同一个对象
==  比数值：两个对象的内容是否相等

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True，内容相等
print(a is b)  # False，不是同一个列表对象
```


# 作用域
Python 的 try、if、for、while 等代码块不会创建新的变量作用域。 password 所属的作用域是当前函数作用域；如果代码不在函数中，就是模块的全局作用域。

```python
try:
    password = input("请输入密码")
except:
    print('x')
else:
    # 可以正常输出
    print(password)

```

```python
for i in range(199):
    # print(i)
    pass

# 可以正常输出, 最终是198
print(i)

```


# 方法文档解读

## range
```markdown

range
@overload
def __new__(cls,
            stop: SupportsIndex,
            /) -> Self
 
Create and return a new object. See help(type) for accurate signature.
```

__new__() -> 负责创建并返回对象

cls -> 表示当前要创建的类，也就是 range 类。它由 Python 自动传入。

stop: SupportsIndex -> 表示 stop 必须是可以作为整数索引的对象，最常见的是整数。

/ -> 表示 / 前面的参数只能按位置传入, 无法使用关键字参数
```python
range(5)       # 正确
range(stop=5)  # 通常会报错
```

self -> 表示返回当前类的实例，也就是返回一个 range 对象。

@overload -> 表示这个函数存在多种合法调用形式。
```markdown
range(stop)
range(start, stop)
range(start, stop, step)

range(stop: SupportsIndex, /)
range(start: SupportsIndex, stop: SupportsIndex, /)
range(start: SupportsIndex, stop: SupportsIndex, step: SupportsIndex, /)
```

## callable
```python
def registerTool(self, name: str, description: str, func: callable):
```
callable 表示"可调用对象"，也就是可以在后面加 () 执行的对象，常见的可调用对象包括普通函数、lambda、类、实现了`__call__`的对象、实例方法


## math.sqrt
```markdown
def sqrt(x: SupportsFloat | SupportsIndex,
         /) -> float
```

SupportsFloat | SupportsIndex -> 支持转换为浮点数，或者支持整数索引。

/ -> 表示 / 前面的参数只能按位置传入, 无法使用关键字参数

float -> 表示返回值类型

## Required
```python
role: Required[Literal["user", "assistant", "system"]]
```
role：字段名
Required[...]：这个字段必须存在
Literal[...]：字段值只能是列出的固定字符串之一
因此 role 只能取："user"、"assistant"、"system"

## Omit = omit
```python
tool_choice: ToolChoiceAutoParam | None | Omit = omit
```
Omit = omit：如果调用者不传这个参数，默认值就是 omit


## multiprocessing
```markdown
self, group: None = None, target, name, args, kwargs, *, daemon
```
group: None = None -> 有默认值


## if isinstance(response_content, list) 和 if isinstance(response_content, List) 有区别吗？
有区别，而且应该使用小写的list，typing.List 主要用于类型标注，不用于运行时类型判断


# 上下文管理器
```python
class MyContext:
    def __enter__(self):
        print("进入 with 代码块")
        return "这是返回值"

    def __exit__(self, exc_type, exc_value, traceback):
        print("退出 with 代码块")


with MyContext() as value:
    print(value)
    print("正在执行代码")

# 进入 with 代码块
# 这是返回值
# 正在执行代码
# 退出 with 代码块
```



执行过程如下：
1. MyContext() 创建对象。
2. 进入 with 时，Python 调用对象的 __enter__()。
3. __enter__() 的返回值被赋给 value。
4. 执行 with 内部的代码。
5. 离开代码块时，Python调用 __exit__()。
即使代码块发生异常，__exit__() 也会执行


# 生成器表达式
```python
if any(word in user_input for word in ["历史", "古迹", "文物", "古城", "博物馆"]):
```
执行过程如下：
1. for word in [...] 会依次取出关键词
    "历史"
    "古迹"
    "文物"
    "古城"
    "博物馆"
2. word in user_input 判断关键词是否存在于字符串中，例如："历史" in "我喜欢历史建筑"
3. any() 判断其中是否至少有一个结果为 True
4. any() 会造成短路，其中一个为True的话就会直接返回

# list
列表拼接
```python
list = [1, 3]
list2 = [2]
print(list + list2)

```


# 方法前加一个下划线
Python 中，方法名前加一个下划线 _，通常表示：这是类或模块内部使用的方法，不建议外部直接调用，未来可能会调整该方法的内容。


# match...case语法

```python
score = 85

match score:
    case value if value >= 90:
        print("优秀")
    case value if value >= 60:
        print("及格")
    case _:
        print("不及格")
```
case _：相当于其他语言中的 default 或 SQL 的 ELSE


# assert断言
```python
age = -1
assert age >= 0, "年龄不能小于 0"
```
如果条件为 True，程序继续执行；如果条件为 False，抛出 AssertionError，或者是指定错误提示


# getattr
getattr是 Python 的内置函数，不需要导入
```python
class User:
    name = "张三"

user = User()

print(user.name)
print(getattr(user, "name"))
# 当属性不存在时设置None, 否则会抛出错误
print(getattr(user, "name", None))
```
如果不提供默认值，属性不存在时会抛出：AttributeError