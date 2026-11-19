# 多模块中功能命名冲突问题
当我们编写了多个模块时, 可能在导入到其他页面时, 会产生一个问题：全局变量、函数、类出现重名情况, 我们把这个情况称之为：命名冲突。
如导入my_module2和my_module3, 里面都封装了一个func方法, 其在导入以后, my_module3中的func方法就会覆盖my_module2中的func方法。

my_module2.py
```python
def func():
    print('my_module2')
```

my_module3.py
```python
def func():
    print('my_module3')
```

导入到其他python文件中, 测试效果：
```python
from my_module2 import func
from my_module3 import func

func()
```

### 解决方案
① 把所有模块的导入方式都写入文件的最上面, 如果发现命名冲突了, 马上和模块的开发人员进行功能核对。

② 给重名的方法进行as重命名
```python
from my_module2 import func as module2_func
from my_module3 import func as module3_func
```

### 模块命名的注意事项
在实际项目开发中, 一定要特别注意：我们自定义的模块名称一定不能和系统内置的模块名称相同, 否则会导致代码无法正常执行。

random.py
```python
import random
print(random.randint(10, 20))
```
randint属于random模块的内置方法, 不可能存在找不到的情况。之所以出现以上问题的主要原因在于：我们的项目中存在了一个与系统模块同名的模块文件, 所有其在引用random模块时, 其执行顺序：
`引入某个模块 => 当前项目中寻找是否有同名的文件 => 如果找到则直接使用, 未找到 => 继续向上寻找  => python解析器`

如何证明：模块的引用一定是按照你说的这个顺序吗？

答：使用`__file__`方法
```python
import random
print(random.__file__)
```