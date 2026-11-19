from idlelib.colorizer import prog_group_name_to_tag

# 字符串

### 字符串定义
字符串是Python中最常用的数据类型。我们一般使用引号来创建字符串。创建字符串很见到那，只要为变量分配一个值即可。

案例：使用单引号或双引号定义字符串变量
```python
str1 = 'abcdefg'
str2 = 'hello world'
print(type(str1))
print(type(str2))
```

案例：使用三引号形式定义字符串变量
> 三引号支持换行操作

```python
name1 = '''I am Tome, Nice to meet you'''
print(type(name1))

name2 = '''I am Jennify
            Nice to meet you'''

name3 = """I am Jeeify
            Nice to meet you"""

```

案例：思考如何使用字符串定义 "I'm Tom"
```python
# 使用单引号情况
str1 = 'I'm Tom'
# 出现以上问题的主要原因子啊与，以上字符串的定义代码出现了语法错误。单引号在字符串定义中必须成对出现，而且
# 在Python解析器在解析代码时，会自动认为第一个单引号和最近的一个单引号是一对。
# 如果一定要在单引号中在放入一个单引号，必须使用反斜杠进行转义
str1 = 'I\'m Tom'


# 在Python中，如果存在多个引号，建议①单引号放在双引号中  ②双引号放在单引号中
str2 = "I'm Tom"
print(str2)

```

### 字符串输入
在Python代码中，我们可以使用input方法来接收用户的输入信息，记住：在Python中，input方法返回的结果是一个`字符串类型`的数据。
```python
name = input('请输入您的姓名：')
age = input('请输入您的年龄：')
address = input('请输入您的住址：')

print(name, age, address)


```


### 字符串的输出

> 普通输出
print(变量名称)
print(变量名称1, 变量名称2, 变量名称3)

> 格式化输出

①百分号（Python2 和 Python3）
```python
name = input('请输入你的姓名：')
age = input('请输入你的年龄：')
address = input('请输入你的住址：')

print('我的名字是%s, 今年%d了, 家里住在%s' %  (name, age, address))

```

②format（Python3）
```python
name = input('请输入你的姓名：')
age = input('请输入你的年龄：')
address = input('请输入你的住址：')

print('我的名字是{}, 今年{}了, 家里住在{}'.format(name, age, address))

```



③f形式（Python3）
```python
name = input('请输入你的姓名：')
age = input('请输入你的年龄：')
address = input('请输入你的住址：')

print(f'我的名字是{name}, 今年{age}了, 家里住在{address}')

```
延伸：
```python
price = input('请输入价格')
print(f'商品价格：{price:.2f}')
```

### 字符串的底层存储结构
在计算机中，Python中的字符串属于序列结构，所以其底层存储占用一段连续的内存空间。

> 索引下标：从0开始

```python
name = 'abcdefg'
print(name[0])
print(name[3])
print(name[6])
```


### 字符串切片
所谓的切片是指对操作的对象截取其中一部分的操作。字符串、列表、元组都支持切片操作。

字符串切片基本语法
> 序列名称[开始位置下标:结束位置下标:步长]

① 不包含结束位置下标对应的数据，正负数均可;
② 步长是选取间隔，正负数均可，正数从左向右，负数从右向左，默认步长为1.

```python
numstr = '0123456789'
# 从2到5开始切片, 步长为1
print(numstr[2:5:1])
print(numstr[2:5])

# 只有结尾的切片, 代表从索引0开始
print(numstr[:5])

# 只有开头的字符串切片, 代表从起始位置开始, 截取到字符串的结尾
print(numstr[1:])

# 获取整个字符串
print(numstr[:])

# 调整步长, 类似求偶数
print(numstr[::2])

# 步长设置为负数，把字符串做翻转
print(numstr[::-1])


# 起始位置和结束位置都是负数, 遵循一个原则，比如是从左向右截取
# 如果没有遵循这个原则的话，不会报错, 就是内容是空的
print(numstr[-4:-1])

# 结束字符为负数
print(numstr[:-1])

```

### 字符串的操作方法



#### 字符串的查找方法

> 基本语法： 字符串.find('xx')

find(): 检测某个子串是否包含在这个字符串中，如果存在返回这个子串开始位置的小标，否则返回-1
index(): 检测某个子串是否包含在这个字符串中，如果存在返回这个子串开始位置的小标，否则报异常
rfind(): 和find功能相同，但是查找方向为右侧开始
rindex(): 和index功能相同，但查找方向为右侧开始
count(): 返回某个子串在字符串中出现的次数

```python
str1 = 'hello world hello linux hello python'
print(str1.find('linux'))
print(str1.find('and'))

# index方法其功能与find方法完全一致, 唯一的区别在于当要查找的子串没有出现在字符串中时, find方法返回-1, index方法则抛错
print(str1.index('apple'))
print(str1.index('pineaple')) 
```

> 基本语法：字符串.rfind('x')

```python
# r = right 代表从右开始查找
# 字符串序列.rfind('xx')
# 字符串序列.rindex('xxx')

filename = '20210310axvu.avatar.png'
# 求出点号在字符串中最后一次出现的位置
index = filename.rindex('.')
print(index)

```

count方法
> 基本语法：字符串.count('x', 开始位置下标, 结束位置下标)

案例：获取字符串中and关键字出现的次数
```python
str = 'hello world and hello linux and hello python'
ands = str.count('and')
print(f'and字符串出现的次数为：{ands}')

# ands = str.count('and', 10, 20) 

```

### 练习题
问题：使用循环嵌套打印正等腰三角形
```python
line = 6

for i in range(1, line + 1):
    print(' ' * (6 - i), end = '')

    z = 1
    while z <= (2 * i - 1):
        print('*', end = '')
        z += 1
    print('')

#      *
#     ***
#    *****
#   *******
#  *********
# ***********

```

#### 字符串的修改方法
所谓修改字符串，指的就是通过函数的形式修改字符串中的数据。

replace(): 返回替换后的字符串
split(): 返回切割后的列表序列
capitalize(): 首字母大写
title(): 所有单词首字母大写
upper() 与 lower()方法： 把字符串全部转换为大写形式、把字符串全部转换为小写形式
lstrip()、rstrip()、strip(): 删除空白字符, 如空格
ljust()、rjust()、center(): 填充字符
join(): 把列表拼接为字符串

replace方法
```python
str1 = 'hello linux an hello linux'
print(str1.replace('linux', 'python'))

# 把字符串中的第一个linux进行替换为python
print(str1.replace('linux', 'python', 1))

```


split方法
作用：对字符串进行切割操作，返回一个list列表类型的数据
```python
str1 = 'apple -banban-orange'
print(str1.split('-'))
```


capitalize方法
作用：把字符串的首字母大写


title方法
作用：把字符串中的所有单词的首字母大写，组成大驼峰
```python
str1 = 'myName'
# 把str1变成首字母大写字符串, 会先把所有单词变成小写, 接着再把首字母变成大写
print(str1.capitalize())

str2 = 'studentmanager'
# 把str2变成大驼峰, 按照空格、下划线、逗号区分每个单词, 如果是合并在一起的单词会被当作是一个是单子
print(str2.titile())

```

lstrip、rstrip、strip
作用：删除字符串的空白字符, 如空格


ljust、rjust、center
作用：返回原字符串左对齐、右对齐以及居中对齐（所谓的左对齐、右对齐、居中对其，就是要填充的字符在哪个位置）
> 基本语法：字符串序列.ljust(长度, 填充字符)

案例：定义一个字符串，要求返回长度为10个字符，不足的使用点号进行填充
```python
# python....
# ####python

str1 = 'python'
print(str1.ljust(10, '.'))
print(str1.rjust(10, '#'))

```

join方法
```python
list = ['a', 'b', 'c']
print('-'.join(list))

```



#### 字符串的判断方法
starswith(): 判断字符串是否以某个子串开头，是则返回True, 否则返回False
endswith(): 判断字符串是否以某个子串结尾，是则返回True, 否则返回False
isalpha(): 判断字符串中的所有字符都是字母，是则返回True, 否则返回False
isdigit(): 判断字符串中的所有字符都是数字, 是则返回True, 否则返回False
isalnum(): 判断字符串(至少一个字符)是否由字母和数字组成，如果字符串所有字符都是字母或数字则返回True, 否则返回False
isspace(): 判断字符串(至少一个字符)中只包含空白, 则返回True, 否则返回False