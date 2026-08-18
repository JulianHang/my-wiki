# 多态

定义：多态是一种使用对象的方式, 子类重写父类方法, 调用不同子类对象的相同父类方法, 可以产生不同的执行结果。

① 多态依赖继承

② 子类方法必须要重写父类方法

> 首先定义一个父类, 可能拥有多个子类对象, 当我们调用一个公共方法时, 传递的对象不同, 其返回的结果不同。


```python
class Fruit(object):
    # 公共方法
    def make_juice(self):
        print('i can make juice')

class Apple(Fruit):
    def make_juice(self):
        print('i can make apple juice')
        
class Banana(Fruit):
    def make_juice(self):
        print('i can make banana juice')
        
class Orange(Fruit):
    def make_juice(self):
        print('i can make orange juice')
        
        
def service(obj: Fruit):
    obj.make_juice()

apple = Apple()
apple.make_juice()

banana = Banana()
banana.make_juice()

orange= Orange()
orange.make_juice()

# 使用多态
for i in (apple, banana, orange):
    service(i)

```