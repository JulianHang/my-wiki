# property

property属性就是负责把一个方法当作属性进行使用, 这样子可以简化代码使用。

定义property属性有两种方式
- 装饰器方式
- 类属性方式

装饰器方式
```python
class Student(object):
    def __init__(self):
        self.__age = 0

    # 当对象调用age属性的时候会执行下面的方法
    @property
    def age(self):
        print('获取属性拉')
        return self.__age

    # 当对象调用age属性设置的时候会调用下面的方法
    @age.setter # @age的名称要跟方法的名称一致
    def age(self, new_age):
        print('设置属性拉')
        if new_age >= 0 and new_age <= 130:
            self.__age = new_age
        else:
            print('成精了')

# 提示：使用装饰器的property属性, 方法名要保持一致

student = Student()
# age = student.age()
age = student.age
print(age)

student.age = 20
age = student.age
print(age)

```


类属性方式
```python
class Student(object):
    def __init__(self):
        self.__age = 0


    def get_age(self):
        print('获取属性拉')
        return self.__age


    def set_age(self, new_age):
        print('设置属性拉')
        if new_age >= 0 and new_age <= 130:
            self.__age = new_age
        else:
            print('成精了')

    age = property(get_age, set_age)

# 提示：使用装饰器的property属性, 方法名要保持一致

student = Student()
# age = student.age()
age = student.age
print(age)

student.age = 20
age = student.age
print(age)

```