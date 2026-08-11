# 字典推导式

> 基本语法
变量 = {key:value for key, value in 序列}

快速合并列表为字典或提取字典中的目标数据。

案例：创建一个字典, 字典key是1-5数字, value是这个数字的2次方。
```python
# dict1 = {1:1, 2: 4, 3:9, 4:16}
dict1 = {i:i ** 2 for i in range(1, 6)}
```

案例：把两个列表合并为一个字典
```python
list1 = ['name', 'age']
list2 = ['Tom', 20]
person = {list1[i]:list2[i] for i in range(len(list1))}
```

案例：提取字典中的目标数据
```python
counts = {'MBP': 268, 'HP': 125, 'DELL': 201}
s = {i:j for i, j in counts.items() if j >= 200}
```