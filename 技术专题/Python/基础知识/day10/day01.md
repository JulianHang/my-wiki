# python模块
python模块, 是一个`python文件`, 以`.py`结尾, 包含了python对象定义和python语句。模块能定义函数、类和变量, 模块里也能包含可执行的代码。

### 模块的分类
模块通常可以分为两大类：内置模块和自定义模块

### 模块的导入方式

1. import模块名
2. from 模块名 import 功能名
3. from 模块名 import *
4. import 模块名 as 别名
5. from 模块名 import 功能名 as 别名

#### import导入模块

基本语法
```python
import 模块名称
或
import 模块名称, 模块名称1, ...
```

使用模块中封装好的方法：
```python
模块名称.方法()
```

案例：使用import导入math模块
```python
import math

# 求数字9的平方根
print(math.sqrt(3))
```

案例：使用import导入math和random模块
```python
import math, random

print(math.pi)
print(random.randint(0, 10))
```

#### 使用from模块名import功能名
提问：已经有了import导入模块, 为什么还需要from模块名import功能名这样的导入方式？

答：import代表导入某个或多个模块中的所有功能, 但是有些情况下, 我们只希望使用这个模块下的某些方法, 而不需要全部导入。这个时候
就建议采用from模块名import功能名

##### from模块名import *
这个导入方式代表导入这个模块的所有功能(等价于import模块名)

```python
from math import *
```

##### from模块名import功能名
```python
from math import sqrt, floor
```

> 以上两种方式都可以用于导入某个模块中的某些方法, 但是在调用具体的方法时, 我们只需要`功能名`即可。

案例：
```python
from math import *
# 或
# from math import sqrt, floor
print(sqrt(9))
```

#### 使用as关键字为导入模块定义别名
在有些情况下, 如导入的模块名称过长, 建议使用as关键字对其重命名操作, 以后在调用这个模块时, 我们就可以使用别名进行操作。

```python
import time as t
# 调用方式
t.sleep(10)
```

#### 使用as关键字为导入功能定义别名
```python
from 模块 import 功能名 as 功能别名
```

案例：
```python
from time import sleep as sl, time as t
# 调用方式
sl(10)
t()

```

> python中, 如果给模块定义别名, 命名规则建议使用大驼峰。