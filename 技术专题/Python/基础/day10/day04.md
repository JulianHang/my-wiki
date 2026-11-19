# 自定义模块
模块的本质在python中就是一个python的独立文件, 里面可以博阿寒全局变量、函数以及类。

> 在python中, 每个python文件都可以作为一个模块, 模块的名称就是文件的名称。也就是说自定义模块名必须要符合标识符命名规则。

### 定义一个自定义模块

案例：在python项目中创建一个自定义文件, 如my_module1.py
```python
def sum_num(num1, num2):
    return num1 + num2

```

### 导入自定义模块
```python
import 模块名称
或
from 模块名称 import 功能名
```

```python
import my_module1
print(my_module1.sum_num(10, 20))
```

### 自定义模块中功能测试
在我们编写完自定义模块以后, 最好在模块中对代码进行提前测试, 以防止有任何异常。

```python
num = 10

def sum_num(num1, num2):
    return num1 + num2

class Person:
    pass

print(__name__)
# 测试代码
print('-' * 40)
print(num)
print(sum_num(10, 20))
p1 = Person()
print(p1)
```

在其他python文件中引入该模块后, 该模块中的测试代码也会跟着一起执行, 为了避免这个问题, 引入一个方法：`__name__`, 其保存的内存就是一个字符串类型的关键字, 关键字是`__main__`。随着运行页面的不同, 其返回结果也是不同的：

① 如果`__name__` 是在当前页面运行时, 其返回结果为`__main__`

② 如果`__name__` 在第三方页面导入运行时, 其返回结果为模块名称

基于以上特性, 我们可以把`__name__`编写在自定义模块中, 其语法如下：

```python
num = 10

def sum_num(num1, num2):
    return num1 + num2

class Person:
    pass

if __name__  == '__main__':
    # 测试代码
    print('-' * 40)
    print(num)
    print(sum_num(10, 20))
    p1 = Person()
    print(p1)
```

`__name__`方法除了可以在自定义模块中测试使用, 还可以用于编写程序的入口：
```python
# 定义一个main方法
def main():
    pass

if __name__ == '__main__':
    main()
```