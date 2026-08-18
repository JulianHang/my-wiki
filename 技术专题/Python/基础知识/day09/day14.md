# 单例模式

```python
class MusicPlayer(object):
    
    def __init__(self, name):
        self.name = name
        
    def start(self):
        print('开始播放音乐')

mp = MusicPlayer('红色高跟鞋')
mp.start()

mp1 = MusicPlayer('xx')
mp1.start()


```

### __new__()方法
使用类名创建对象时, python解释器首先会调用`__new__`方法为对象分配空间, new 是一个由object基类提供的内置的静态方法, 主要作用有两个：
1、 在内存中为对象分配空间
2、返回对象的引用

python解析器获得对象的引用后, 将引用作为第一个参数, 传递给init方法。重写`__new__`方法的代码非常固定, 一定要使用`return super().new(cls)`, 否则python解释器得不到分配了空间的对象引用,
就不会调用对象的初始化方法。

> __new__方法是一个静态方法, 在调用时, 要求将自身类信息cls作为参数传递到这个方法中, 这个方法属于object类中的一个静态方法。

```python
class MusicPlayer(object):
    # 定义一个类属性, 如instance, 用于记录之前实例化对象返回的内存引用
    instance = None
    
    def __new__(cls, *args, **kwargs):
        # 判断实例化时有没有分配过内存空间
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    
    
    def __init__(self, name):
        self.name = name
        
p1 = MusicPlayer('x')
print(p1)

p2 = MusicPlayer('y')
print(p2)

```