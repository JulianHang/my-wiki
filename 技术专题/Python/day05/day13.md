# 数据序列中的公共方法

+ : 合并, 支持字符串、列表、元组
* : 赋值, 支持字符串、列表、元组
in : 元素是否存在, 字符串、列表、元组、字典
not in : 元素是否不存在, 字符串、列表、元组、字典
len(): 计算容器中元素的个数
del或del(): 根据索引下标删除指定元素
max(): 返回容器中元素的最大值
min(): 返回容器中元素的最小值
range(start, end, step): 生成从start到end的数字, 步长为step, 供循环使用
enumerate(): 函数用于将一个可遍历的数据对象(如列表、元组、字符串)组合为一个索引序列, 同时列出数据和数据下标, 一般在for循环当中使用
  

```python
str1 = 'hello'
str2 = 'world'
print(str1 + str2)

list1 = ['刘备', '关羽']
list2 = ['诸葛亮', '赵云']
print(list1 + list2)

tuple1 = (10, 20, 30)
tuple2 = (30, 40)
print(tuple1 + tuple2)
```

```python
print('-' * 10)

list1 = ['*']
print(list1 * 10)

tuple1 = (10, )
print(tuple1 * 10)
```


len方法
```python
str1 = 'hello world'
print(f'字符串的长度为{len(str1)}')


list1 = [10, 20, 30]
print(f'列表的长度为{len(list1)}')
```


del方法
```python
list1 = ['吕布', '董卓', '貂蝉']
del list1[1]
print(list1)

dict1 = {'name': '白龙马', 'age': 23}
del dict1['age']
print(dict1)
```

max方法
```python
num1 = int(input('请输入第一个数：'))
num2 = int(input('请输入第二个数：'))
num3 = int(input('请输入第三个数：'))
list1 = [num1, num2, num3]
print(max(list1))
print(min(list1))
```

enumerate方法
```python
list1 = [10, 20, 30, 40, 50]
n = 1
for i in list1:
    print(f'第{n}个数:{i}')
    n += 1

print('-'* 40)
for key, value in enumerate(list1):
    print(f'第{key + 1}个数:{value}')
```

