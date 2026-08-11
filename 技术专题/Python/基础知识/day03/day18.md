# for循环
for循环结构主要用于（序列 =》字符串、列表、元素、集合以及字典）类型数据的遍历操作

```python
for 临时变量 in 序列：
    重复执行的代码1
    重复执行的代码2
```

### 案例
使用for循环遍历字符串itheima

```python
for i in 'itheima':
    print(i)
```
for循环功能非常强大，可以自动判断序列的长度，长度为多少，则for循环就循环多少次。每次循环时，系统会自动
将序列中的每个元素赋值给变量i，赋值完成后，for循环内部会自动更新计数器，向后移动一位，继续循环，直至元素全部循环结束。

### range方法
python2 range函数返回的是列表，而在python3中range函数返回的是一个可迭代对象，而不是列表类型，所以打印的时候不会打印列表。
主要作用：用于生成一段连续的内容，从0到9
```python
# 基本语法
# range(stop)

# start：计数从start开始，默认是从0开始，例如range(5) 等价于 range(0, 5)
# stop：计数从stop结束，但不包括stop，例如 range(0, 5) 是 [0,1,2,3,4] 没有5
# step： 步长，默认为1，例如，range(0, 5) 等价于 range(0, 5, 1)
# rnage(start, stop[, step])  

```
> range有一个口诀：顾头不顾尾，包含头部信息，但是不包含尾部信息，如range(10)，则返回 0 -9 之间的序列。

案例1：使用range循环，求1~100的和
```python
result = 0
for i in range(1, 101):
    result += i
print(f'1~100的和为{result}')
```

案例2：使用for循环，求1~100之间所有偶数的和
```python
result = 0
for i in range(1, 101):
    if i % 2 == 0:
        result += i
print(f'1~100之间所有偶数的和{result}')
```

案例3：遇到字符e，则终止整个循环
```python
str1 = 'itheima'
for i in str1:
    if i == 'e':
        break
    print(i)
```

案例4：遇到字符e，则跳过本次循环，继续下一次循环
```python
str1 = 'itheima'
for i in str1:
    if i == 'e':
        continue
    print(i)
```

综合案例：使用for循环实现用户名+密码认证
```python
trycount = 0 
for i in range(3):
    trycount += 1
    
    username = input('请输入您的登录账号')
    password = input('请输入您的登录密码')
  
    if username  == 'admin':
        if password == 'admin888':
            print('恭喜你，登录成功')
            break
        else:
            print(f'密码错误，你还有{3 - trycount}次机会')
    else:
        print(f'账号错误，你还有{3 - trycount}次机会')
         

```