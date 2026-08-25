# 类装饰器

```python
class MyDecorator(object):
    def __init__(self, func):
        self.__func = func

    # 实现__call__这个方法, 让对象变成可调用的对象, 可调用的对象能够像函数使用
    def __call__(self, *args, **kwargs):
        print('课已讲完')
        self.__func()

@MyDecorator  # @MyDecorator => show = MyDecorator(show)
def show():
    print('快要下雪了')

# 执行MyDecorator类创建实例对象, show() => 对象()
show()

```

拓展
```python
class AAA(object):
    pass

    def __call__(self, *args, **kwargs):
        pass

a = AAA()
# 实现__call__就能把对象像函数一样调用
a()
```

函数之所以能够调用是因为函数内部使用了`__call__`
```python
def mytest():
    print('哈哈')

# 输出中带有 __call__方法
print(dir(mytest))
```