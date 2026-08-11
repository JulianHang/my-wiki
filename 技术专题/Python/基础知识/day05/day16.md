# 列表集合字典推导式
推导式是可以从一个数据序列构建另一个新的数据序列的结构体, 共有3种推导式：列表推导式、集合推导式、字典推导式。

案例：创建一个0-9的列表
```python
i = 0
list1 = []
while i <= 9:
    list1.append(i)
    i += 1

list2 = []
for i  in range(0, 10):
    list2.append(i)

```


### 列表推导式

> 基本语法
变量名 = [表达式 for 变量 in 列表]
变量名 = [表达式 for 变量 in 列表 if 条件]

```python
list1 = [i for i in range(10)]
```
执行原理：[i for i in range(10)]
列表推导式先运行表达式右边的内容, 第一次遍历时：i=0, 其得到变量i的结果后, 会放入最左侧的变量i中, 这个时候列表中就是[0], 当第二次遍历时, i = 1, 其得到变量i的结果后, 会放入最左侧的变量i中, 这个时候列表中就是[0, 1]
...., 以此类推, 当到最后一次时, 列表中的数据会是[0,1,2,3,4,5,6,7,8,9]

#### 列表推导式 + if 条件判断
在使用列表推导式时, 除了可以使用for循环, 我们还可以在其遍历的过程中, 引入if条件判断。

[表达式 for 变量 in 列表 if 条件判断]

等价于
for 变量 in 序列:
    if 条件判断

```python
list1 = [i for i in range(10) if i % 2 == 0]
```
执行原理：[i for i in range(10) if i % 2 == 0]
循环x序列, 把元素赋值给 i, 判断 num % 2 == 0, 条件为真时，计算前面的表达式 num, 将结果放入新列表, 条件为假时跳过该元素。


[num if num > 3 else 0 for num in nums]

等价于
```python
result = []

for num in nums:
    if num > 3:
        result.append(num)
    else:
        result.append(0)
```

简单区分：
for 后面的 if：过滤元素;
表达式中的 if...else：决定每个元素生成什么结果;

#### for循环嵌套列表推导式

```python
for 临时变量 in range(n):
    for 临时变量 in range(n):
```

> 基本语法
变量 = [表达式 for 临时变量 in 序列 for 临时变量 in 序列]


```python
list = [(i, j) for i in range(1, 3) for j in range(3)]
```