# 闭包
在函数嵌套的前提下, 内部函数使用了外部函数的变量, 并且外部函数返回了内部函数, 我们把这个使用外部函数变量的内部函数称为`闭包`

### 闭包的构成条件
通过闭包的定义, 我们可以得知闭包的形成条件：

1. 在函数嵌套的前提下
2. 内部函数使用了外部函数的变量(包括外部函数的参数)
3. 外部函数返回了内部函数

```python
def func_out():
    num1 = 10
    def func_inner(num2):
        result = num1 + num2
        print('结果：', result)
    return func_inner


new_func = func_out()
# 执行闭包
new_func(1)
new_func(10)
```

### 闭包的作用
闭包可以保存外部函数内的变量, 不会随着外部函数调用完而销毁

> 由于闭包引用了外部函数的变量, 则外部函数的变量没有及时释放, 消耗内存。

### 闭包的使用

```python
def config_name(name):
    def inner(msg):
        print(name + " : " + msg)
        
    print(id(inner))
    return inner

tom = config_name('tom')
jerry = config_name('jerry')

# 如果执行tom闭包, 因为已经保存了name参数, 那么以后在输入的时候都是, tom:xx
tom('哥们, 过来一下, 我们一起玩耍')
jerry('打死都不去')
tom('我不吃你')
jerry('谁相信你')
```

### 修改闭包内的外部变量
```python
def func_out():
    num1 = 10
    def func_inner():
        nonlocal num1
        num1 = 20
        result = num1 + 10
        print(result)
    print('修改前的外部变量', num1)
    func_inner()
    print('修改后的外部变量', num1)

func_out()
```

