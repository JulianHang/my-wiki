# 字典
特点：
① 使用花括号：{}
② 数据为键值对形式出现：{key: value}, 在同一个字典中, key必须是唯一
③ 各个键值对之间用逗号隔开

```python
# 有数据字典
dict1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}
# 空字典
dict2 = {}
dict3 = dict()
```


### 字典的增操作

> 基本语法：字典名称[key] = value
如果这个key存在则修改这个key对应的值, 如果key不存在则新增此键值对。

```python
person = {}
person['age'] = 20


```

### 字典的删操作
① del 字典名称[key]: 删除指定key

② clear: 清空字段字典里的所有key

```python
person = {'name ': '王大锤', 'age': 28, 'address': '北京市海淀区'}
del person['age']
print(person)
```


### 字典的修改操作

> 基本语法：字典名称[key] = value
如果这个key存在则修改这个key对应的值, 如果key不存在则新增此键值对。

案例：定义一个字典, 里面有name、age以及address, 修改address这个key对应的值

```python
person = {'name': '孙悟空', 'age': 60, 'address': '花果山'}
person['address'] = '黑马'
print(person)
```


### 字典的查询操作
① 查询方法：使用具体的某个key查询数据, 如果未找到, 则直接报错
>  字典序列[key]

② 查询方法
get(key， 默认值): 如果当前查找的key不存在则返回第二个参数(默认值), 如果省略第二个参数, 则返回None
keys(): 以列表形式返回字典的所有键
values(): 以列表形式返回字典的所有值
items(): 以列表返回可遍历(键, 值)元组数组

get方法
```python
cat = {'name': 'Tom', 'age': 5, 'address': '美国纽约'}
name = cat.get('name')
age = cat.get('age')
address = cat.get('address')
gender = cat.get('gender', 'male')
print(f'姓名：{name}, 年龄：{age}, 地址：{address}, 性别：{gender}')
```

keys、values方法
```python
person = {'name': '貂蝉', 'age': 18}
print(person.keys())
print(person.values())
```

items方法
```python
# dict_items([('name', '貂蝉'), ('age', 18)])  列表里的元组
person = {'name': '貂蝉', 'age': 18}
print(person.items())

# ('name', '貂蝉')  ('age', 18)
for i in person.items():
    print(i)
    
for key, value in person.items():
    print(key, value)

```