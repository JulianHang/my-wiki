# 集合
是一个无序的不重复元素序列。可以像元组一样, 设置不可改变的类型。也可以默认像字典, 列表一样, 可以迭代改变。其中的元素可以是列表、元组、字典。
[天生去重]

> 基本语法：创建集合使用{}或set(), 但是如果要创建空集合只能使用set(), 因为{}用来创建空字典。

```python
s1 = {10, 20, 30, 40}
print(s1)
print(type(s1))

s2 = {'刘备', '曹操', '孙权', '曹操'}
print(s2)

s3 = {}
s4 = set()
print(type(s3))
print(type(s4))

```


#### 集合的增操作
① add方法: 向集合中增加一个元素(单一)

```python
students = set()
students.add('lize')
students.add('ss')
print(students)
```

② update方法: 向集合中增加序列类型的数据(字符串、列表、元组、字典)

```python
students = set()
list1 = [10, 20, 30]
students.update(list1)
print(students)
```

#### 集合的删除操作
① remove()方法: 删除集合中的指定数据，如果数据不存在则报错

② discard()方法: 删除集合中的指定数据, 如果数据不存在不会报错

③ pop()方法: 随机删除集合中的某个数据, 并返回这个数据

```python
products = {'萝卜', '白菜', '水蜜桃', '奥利奥'}
products.remove('白菜')
products.discard('玉米')
del_product = products.pop()  # 随机删除元素
print(del_product)
```

#### 集合的查询操作
① in: 判断某个元素是否在集合中, 如果在则返回True, 否则返回False

② not in: 判断某个元素是否不在集合中, 如果不在返回True, 否则返回False

③ 集合的遍历操作

```python
s1 = {'a', 'b', 'c'}
if 'a' in s1:
    print('在集合中')
else:
    print('不在集合中')

# 对集合进行遍历操作
for i in s1:
    print(i)

```