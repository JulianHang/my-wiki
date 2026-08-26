# 上下文管理器
一个类只要实现了`__enter`和`__exit__`这两个方法, 通过该类创建的对象我们就称之为上下文管理器。上下文管理器可以使用with语句, with语句之所以这么强大, 背后是由上下文管理器做支撑的, 也就是说刚才使用open函数创建的文件对象就是一个上下文管理器对象。

```python

# 自定义上下文管理器
class File(object):
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode


    def __enter__(self):
        # 负责返回操作对象资源, 比如：文件对象, 数据库连接对象
        self.file = open(self.file_name, self.file_mode)
        return self.file

    # 当with语句执行完成以后自动执行__exit__方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 负责释放对象资源, 比如：关闭文件, 关闭数据库连接对象
        print('over')
        self.file.close()

with File('1.txt', 'r') as file:
    file_data = file.read()
    print(file_data)
```

### 上下文管理器的另外一种实现方式
假如想要让一个函数成为上下文管理器, python提供了一个@contextmanager的装饰器, 更进一步简化了上下文管理器的实现方式, 通过yield将函数分隔成两部分, yield 上面的语句在`__enter__`方法中执行, yield下面的语句在`__enter__`方法中执行, 紧跟着在yield后面的参数是函数的返回值。

```python
from contextlib import contextmanager

# 加上装饰器这个代码, 那么下面函数创建的对象就是一个上下文管理器
@contextmanager
def my_open(file_name, file_mode):
    try:
        file = open(file_name, file_mode)
        # yield关键字之前的代码可以认为是上文方法, 负责返回操作对象资源
        yield file
    except Exception as e:
        print(e)
    finally:
        print('over')
        # yield关键字后面的代码可以认为是下文方法, 负责释放操作对象的资源
        file.close()

# 普通函数不能结合with语句使用, with语句是要结合上下文管理器
with my_open('1.txt', 'r') as file:
    file_data = file.read()
    print(file_data)

```