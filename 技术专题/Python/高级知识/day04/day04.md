# 生成器

根据程序员制定的规则循环生成数据, 当条件不成立时则生成数据结束。数据不是一次性全部生成出来, 而是使用一个, 再生成一个, 可以节约大量的内存。

### 创建生成器的方式

1. 生成器推导式
2. yield关键字


生成器推导式：
```python
my_generator = (value * 2 for value in range(3))
print(my_generator)

# 生成器取值使用next函数获取生成器中的下一个值
value = next(my_generator)
print(value)

value = next(my_generator)
print(value)

value = next(my_generator)
print(value)

# 当生成器已经没有值时, 会抛出StopIteration, 表示生成器生成数据完毕
value = next(my_generator)
print(value)

### =====>
# for循环内部循环调用next函数获取生成器中的下一个值, 当出现异常时, for循环内部自动进行了异常捕获
for value in my_generator:
    print(value)
```

yield关键字：
```python
# 在函数内部看到有yield关键字, 那么这个 函数就是生成器了
def my_generator():
    for i in range(3):
        print('开始生成数据啦...')
        # 当程序执行到yield关键字的时候代码会暂停并把结果返回, 再次启动生成器的时候会在暂停的位置上继续往下执行
        yield i
        print('上一次的数据生成完了...')



result = my_generator()
print(result)

# 获取生成器的下一个值
value = next(result)
print(value)


# 获取生成器的下一个值
value = next(result)
print(value)

# 获取生成器的下一个值
value = next(result)
print(value)

# 生成器把所有数据生成完毕后, 再次启动生成器会抛出一个StopIteration异常
value = next(result)
print(value)

# ====>
for i in result:
    print(i)
```


### 生成器的使用场景


```python
def fibonacci(num):
    # 初始化前两个值
    a = 0
    b = 1
    # 记录每次生成个数的索引
    current_index = 0
    while current_index < num:
        result = a
        # 条件成立交换两个变量的值
        a, b = b, a + b
        current_index += 1
        yield result

# 创建生成器
f = fibonacci(5)

value = next(f)
print(value)

```