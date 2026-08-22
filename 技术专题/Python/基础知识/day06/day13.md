# global关键字
思考：如果有一个数据, 在函数A和函数B中都想要使用, 怎么办？

答：将整个数据存储在一个全局变量里面。

```python
num = 10

def func():
    num = 20

func()
print(num)
```
最终结果：弹出10, 所以由运行结果可知, 在函数体内部理论上是没有办法对全局变量进行修改的, 所以一定要进行修改, 必须使用
`global` 关键字

```python
num = 10

def func():
    global num
    num = 20

func()
print(num)
```

如果是可变类型的话, 直接使用内置的方法进行修改元素, 无需加`global`
```python
g_list = []

def add_data():
    for i in range(3):
        g_list.append(i)

add_data()
```
