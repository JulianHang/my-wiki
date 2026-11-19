from functools import reducefrom functools import reduce

# 高阶函数
把函数作为参数传入, 这样的函数称为高阶函数。

```python
def fn1(num1, num2):
    return abs(num1) + abs(num2)

def fn2(num1, num2):
    return round(num1) + round(num2)

# 简化代码
def fn(num1, num2, f):
    # f代表要传入的参数, 是一个函数, 如abs 或 round
    return f(num1) + f(num2)

# 绝对值求和
fn(-10, 10, abs)
# 四舍五入
fn(10.2, 6.9, round)


```
### 内置高阶函数

#### map函数

`map(func, list)` 将传入的函数变量func作用到list变量的每个元素中, 并将结果组成新的列表(python2)/迭代器(python3) 返回

```python
def func(n):
    return n ** 2

list1 = [1, 2, 3]
list2 = list(map(func, list1))
print(list2)


```

### reduce函数
`reduce(func, lst)` 其中func函数必须有两个参数, 每次func计算的结果继续和序列的下一个元素做累积计算。

```python
from functools import reduce

list1 = [1, 2, 3]
def func(a, b):
    return a + b

sum2 = reduce(func, list1)
print(sum2)
```


### filter 函数
`filter(func, lst)` 函数用于过滤序列, 过滤掉不符合条件的元素, 返回一个filter对象。如果要转换成列表, 可以用list()来转换


```python

def func(n):
    return n % 2 == 0   # True 或者 False

list1 = [1, 2, 3, 4, 5]
result = filter(func, list1)
print(list(result))

```