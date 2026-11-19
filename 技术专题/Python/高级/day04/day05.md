# 深拷贝和浅拷贝

copy函数是浅拷贝, 只对可变类型的第一层对象进行拷贝, 对拷贝的对象开辟ixn的内存空间进行存储, 不会拷贝对象内部的子对象。

### 浅拷贝
```python
import copy

num1 = 1
num2 = copy.copy(num1)

# 查看后两个打印的内容内存地址没有发生变化, 说明没有对对象进行拷贝, 也就说没有开辟新的内存空间
print('num1：', id(num1), 'num2：', id(num2))

# 对于不可变类型进行浅拷贝实际上是对引用的一个拷贝, 两个变量指定的是同一个内存地址

my_tuple1 = (3, 5)
my_tuple2 = copy.copy(my_tuple1)
print('my_tuple1：', id(my_tuple1), 'my_tuple2：', id(my_tuple2))

# 得知结论：浅拷贝不会对不可变类型进行拷贝, 也就说不会开辟新的内存空间

# 可变类型：列表、字典、集合
my_list1 = [1, 3, [4, 6]]
my_list2 = copy.copy(my_list1)
print(my_list2)
print('my_list1：', id(my_list1), 'my_list2：', id(my_list2))
my_list1.append(5)
print(my_list1, my_list2)

print('my_list1[2]：', id(my_list1[2]), 'my_list2[2]：', id(my_list2[2]))
my_list1[2].append(7)
print(my_list1, my_list2)

```

### 深拷贝
deepcopy函数是深拷贝, 只要发现对象有可变类型就会对该对象到最后一个可变类型的每一层对象进行拷贝, 对每一层拷贝的对象都会开辟新的内存空间进行存储。

```python
import copy

num1 = 1
num2 = copy.deepcopy(num1)

print('num1：', id(num1), 'num2：', id(num2))

str1 = 'hello'
str2 = copy.deepcopy(str1)
print('str1：', id(str1), 'str2：', id(str2))

my_tuple1 = (1, [1, 2])
my_tuple2 = copy.deepcopy(my_tuple1)
# 整体会拷贝
print('my_tuple1：', id(my_tuple1), 'my_tuple2：', id(my_tuple2))
# 不可变类型不会拷贝
print('my_tuple1[0]：', id(my_tuple1[0]), 'my_tuple2[0]：', id(my_tuple2[0]))
# 可变类型会拷贝
print('my_tuple1[1]：', id(my_tuple1[1]), 'my_tuple2[1]：', id(my_tuple2[1]))


my_tuple2[1].append(4)
print(my_tuple1, my_tuple2)

# 如果发现元组里面有可变类型, 那么会对元组进行拷贝和子元素列表进行拷贝, 拷贝后都会产生一个新的内存空间
# 但是不可变类型不会进行拷贝, 因为不可变类型不允许在原有内存空间的基础上修改数据
# 所以拷贝没有意义, 因为每次修改数据内存地址都会发生变化

# 可变类型：列表、字典、集合, 对深拷贝来说也会进行拷贝, 如果发现子对象也是可变类型, 也会进行拷贝,
# 拷贝后会开辟新的内存空间存储拷贝后的对象
my_list1 = [1, [2, 3]]
my_list2 = copy.deepcopy(my_list1)
print('my_list1：', id(my_list1), 'my_list2：', id(my_list2))

```