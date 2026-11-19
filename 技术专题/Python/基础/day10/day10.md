# 案例

student.py
```python
class Student():

    def __init__(self, name, age, mobile):
        self.name = name
        self.age = age
        self.mobile = mobile

    def __str__(self):
        return f'姓名：{self.name}, 年龄：{self.age}, 电话号码：{self.mobile}'

```

studentManager.py
```python
class StudentManager(object):
    
    def __init__(self):
        self.student_list = []

    def load_student(self):
        pass
    
    @staticmethod
    def show_help():
        print('-' * 40)
        print('xx管理系统2.0')
        print('1. 添加学员信息')
        print('2. 删除学员信息')
        print('-' * 40)
    
     
    def add_student(self):
        pass
    
    def del_student(self):
        pass
    
    def mod_student(self):
        pass
    
    def show_student(self):
        pass
    
    def show_all(self):
        pass
    
    def save_student(self):
        pass
    
        
    def run(self):
        # 调用一个学员加载方法, 用于加载文件中的学员信息
        self.load_student()
        while True:
            # 显示帮助信息
            self.show_help()
            # 提示用户输入要操作的功能编号
            user_num = int(input('请输入要操作功能的编号：'))
            if user_num == 1:
                self.add_student()
            elif user_num == 2:
                self.del_student()
            elif user_num == 3:
                self.mod_student()
            elif user_num == 4:
                self.show_student()
            elif user_num == 5:
                self.show_all()
            elif user_num == 6:
                self.save_student()
            elif user_num == 7:
                break
            else:
                print('输入错误, 请重新输入...')
            

```

main.py
```python
# 从studentManager模块中导入StudentManager类
from studentManager import StudentManger

if __name__ == '__main__':
    studentManager = StudentManger()
    studentManager.run()

```