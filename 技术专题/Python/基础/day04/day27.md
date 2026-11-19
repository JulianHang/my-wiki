# 列表

### 列表的定义

```python
# 列表序列名称 = [列表中的元素1, 列表中的元素2, 列表中的元素3]

list1 = ['a', 'b', 'c']
# 列表支持直接打印
print(list1)
```

> 注意：列表可以一次性存储多个数据，且可以为不同的数据类型


#### 列表的查询
列表在计算机中的底层存储形式，列表和字符串一样，在计算机内存中都占用一段连续的内存地址，我们想访问列表中的每个元素，都可以通过索引下标的方式进行获取。

```python
list1 = ['apple', 'banba', 'pineapple']
print(list1[0])
```

index(): 指定数据所在位置的下标
count(): 统计指定数据在当前列表中出现的次数
in: 判断指定数据在某个列表序列，如果存在则返回True, 否则返回False
not in: 判断指定数据不在某个列表序列, 如果不存在则返回True, 否则返回False

```python
list1 = ['apple', 'banba', 'a']
print(list1.index('banba'))

print(list1.count('x'))

list3 = ['192.168.1.15', '192.168.23.2']
if '192.168.1.15' in list3:
    print('匿名黑名单IP, 禁止访问')
else:
    print('正常IP, 可以访问')

```

#### 列表的增加
append(): 增加指定数据到列表中
extend(): 列表结尾追加数据, 如果数据是一个序列, 则将这个序列的数据逐一添加到列表
insert(): 指定位置新增数据


append方法
```python
names = ['孙悟空', '唐曾', '猪八戒']
names.append('沙僧')
print(names)

```

> 列表追加数据的时候, 直接在原列表里面追加了指定数据, 即为修改了原列表, 故列表为可变类型数据。

extend方法
```python
# ['Tom', 'Rose', 'Jack', 'J', 'e', 'n', 'n', 'i', 'f', 'y']
names = ['Tom', 'Rose', 'Jack']
# names.extend('Jennify')
# print(names)

# 建议：使用extend犯法将两个列表合并
list2 = ['Hack', 'Jennify']
names.extend(list2)
print(names)

```

insert方法
```python
names = ['薛宝钗', '林黛玉']
names.insert(1, '贾宝玉')
print(names)
```


#### 列表的删除
del 列表[索引下标]: 删除列表中的某个元素
pop(): 删除指定下标的数据(默认为最后一个), 并返回删除的数据
remove(): 移除列表中某个数据的第一个匹配项
clear(): 清空列表, 删除列表中的所有元素，返回空列表

del方法
```python
names = ['a', 'b', 'c']
del names[1]
print(names)

```

pop方法
```python
names = ['a', 'b', 'c']
del_name = names.pop()
# 或
# del_name = names.pop(0)
print(del_name)
print(names)
```


remove方法
```python
fruit = ['apple', 'banba', 'pipne']
fruit.remove('apple')
print(fruit)
```

clear方法
```python
names = ['貂蝉', '吕布', '董卓']
names.clear()
print(names)
```


#### 列表的修改
列表[索引下标] = 修改后的指： 修改列表中的某个元素
reverse(): 将数据序列进行倒叙排列
sort(): 对列表序列进行排序
copy(): 对列表序列进行拷贝

```python
list1 = ['a', 'b', 'c', 'd']
list1[3] = 'f'
print(list1)

list2 = [1, 2, 3, 4]
list2.reverse()
print(list2)

list3 = [10, 50, 20, 30]
list3.sort()  # 默认是升序排列
# 或 list3.sort(reverse=True) 降序排列
print(list3)

list4 = ['x', 'y']
list5 = list4.copy()
print(list5)

```

#### 列表的循环遍历
使用while或for循环对列表中的每个数据进行打印输出
```python
list1 = ['a', 'b', 'c']
for i in list1:
    print(i)


i = 0 
while i < len(list1):
    print(list1[i])
    i += 1
```

#### 列表的嵌套
列表中还有一个列表, 在其他编程语言中, 称之为二维数据或多维数据

应用场景：要存储班级一、二、三班级，三个班级学生姓名，且每个班级的学生姓名在一个列表

```python
students = [['张三', '李四'], ['王五', '赵六'], ['田七', '孙八']]

print(students[0][1])

for i in students:
    print(i)
```

#### 案例

幸运数字6:输入任意数字，如数字8，生成nums列表，元素值为1~8，从中选取幸运数字移动到新列表lucky，打印nums与lucky。
```python
import random

digit = int(input('数字：'))

list = []
for i in range(1, digit + 1):
    list.append(i)

lucky = []
index = random.randint(0, len(list))
lucky_num = list.pop(index)
lucky.append(lucky_num)

```



列表嵌套：有3个教室[[],[],[]], 8名讲师['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], 将这8名讲师随机分配到3个教室中
```python
import random

class_rooms = [[], [], []]
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

for teacher in teachers:
    class_index = random.randint(0, 2)
    class_rooms[class_index].append(teacher)

print(class_rooms)


```

