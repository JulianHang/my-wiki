# python包
包将有联系的模块组织在一起, 即放在同一个文件夹下, 并且在这个文件夹创建一个名字为`__init__.py`文件, 那么这个文件夹就称之为包。

### 在包中创建多个模块

在mypackage包中创建多个模块：my_module1和my_module2

my_module1.py
```python
print('my_module1')
def func1():
    print('my_module1_func1')
```

my_module1.py
```python
print('my_module2')
def func2():
    print('my_module2_func2')
```

### 在项目代码中导入包package

方式一：使用import导入包

```python
import 包名.模块名

# 调用模块中的方法
包名.模块名.方法名()
```


案例：

test.py
````python
import mypackage.my_module1
import mypackage.my_module2

# 调用方法
mypackage.my_module1.func1()
mypackage.my_module2.func2()
````


方式二：使用from导入包

> 必须在`__init__.py`文件中添加`__all__=[]`, 控制允许导入的模块列表。

```python
from 包名 import 模块名
# 调用模块方法
模块名.方法名()
```
可以这么理解, 实际上就是找到包名, 导出模块名

案例：

__init__.py文件
```python
# 这个限制是对 from mypackage import * 有限制, 如果是在代码中直接导入指定模块的话, 没有效果
__all__ = ['my_module1']

```

test.py
```python
from mypackage import my_module1
from mypackage import my_module2

my_module1.func1()
my_module2.func2()
```
