from operator import truediv

# 布尔类型
布尔类型是与逻辑相关一种数据类型，只有两个值：True(真)与False(假)

```python
flag = True
print(flag)
print(type(flag))
```

其实再Python中，很多程序的返回结果也可以是True或者False，比如 isinstance()


```python
num = 10
print(isinstance(num, int)) # True
print(isinstance(num, bool)) # False
```


# 字符串
在Python变量定义中，如果其赋值的内容是通过单引号或双引号引起来的内容就是字符串str类型
```python
msg = '这家伙很懒， 什么都没有留言...'
print(type(str))
print(isinstance(str, str))
```

# 其它类型
### 列表类型

```python
list1 = [10, 20, 30, 40]
print(type(list1))
```

### tuple元组类型
```python
tuple1 = (10, 20,30,40)
print(type(tuple1))
```

### set集合类型，去重
```python
set1 = {10, 20, 30}
print(type(set1))
```

### dict字典类型，查询、搜索
```python
dict1 = {'name': 'itemiam', 'age': '18'}
print(type(dict1))
```

# 调试
遇到小闪电图标就代表这一行，可能出错了



