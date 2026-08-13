# 面向对象的案例

案例：定义学员信息类, 包含姓名、成绩属性, 定义成绩打印方法(90分及以上显示优秀, 80分及以上显示良好, 70分及以上显示中等, 60分及以上显示合格, 60分以下显示不及格)

```python
class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        result = ''
        score = self.score
        if score >= 90:
            result = '优秀'
        elif 80 <= score < 90:
            result = '良好'
        elif 70 <= score < 80:
            result = '中等'
        elif 60 <= score < 70:
            result = '合格'
        else:
            result = '不及格'
        return f'{self.name}的成绩{result}'

s1 = Student('a', 30)


```

案例：小明体重75公斤, 小明每次跑步会减掉0.5公斤, 小明每次吃东西体重增加1公斤

```python
class Person():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight = self.weight - 0.5

    def eat(self):
        self.weight = self.weight + 1

    def __str__(self):
        return f'{self.name}, 体重：{self.weight}'



```
