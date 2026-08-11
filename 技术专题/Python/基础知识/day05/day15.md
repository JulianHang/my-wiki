# 序列类型之间的相互转换

list(): 把某个序列类型的数据转化为列表, 值得注意的是, 字典在转换过程中, 只会保留字典中的key, value会被自动忽略
tuple(): 把某个序列类型的数据转化为元组

list方法
```python
# 元组转化为列表
tuple1 = (10, 20, 30)
print(list(tuple1))

# 集合转化为列表
set1 = {'a', 'b', 'c', 'd'}
print(list(set1))

# 字典转化为列表
dict1 = {'name': '张三', 'age': 19}
print(list(dict1))
```

tuple方法
```python
# 列表转换为元组
list1 = [10, 20, 30]
print(tuple(list1))

# 集合转换为元组
set1 = {10, 20, 30}
print(tuple(set1))
```

set方法：将某个序列转换成集合, 可以快速完成列表去重, 集合不支持下标

```python
list1 = ['a', 'b', 'c', 'd']
print(set(list1))

tuple1 = (10, 20, 30)
print(set(tuple1))
```