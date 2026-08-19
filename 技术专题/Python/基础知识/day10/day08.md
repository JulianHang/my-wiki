# __all__
主要功能：限制使用模块中的某些功能, 也就是说你导入后可以使用的方法只能是`__all__`封装好的方法。

案例：
my_module.py
```python
__all__ = ['func']

def func():
    print('func')

def func1():
    print('func1')
```

test.py
```python
from my_module import *

```