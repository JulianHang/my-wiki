# 综合案例：通讯录管理系统
需求：开一个通讯录的管理系统, 主要用于存储班级中同学的信息(姓名、年龄、电话)

```python
students = [{'name': '刘备', 'age': 18, 'mobile': '10086'}, {'name': '张飞', 'age': 16, 'mobile': '10010'}]
```

代码

```python
students = []
print('-' * 40)
print('欢迎使用xxx通讯录管理系统V1.0')
print('-' * 40)

user_num = int(input('请输入您要进行的操作编号：'))
if user_num == 1:
    student = {}
    student['name'] = input('请输入学员的姓名')
    student['age'] = int(input('请输入学员的年龄'))
    student['mobile'] = input('请输入学员的电话')
    students.append(student)
    print(students)
    pass
elif user_num == 2:
    name = input('请输入要删除的学员信息')
    for i in students:
        if i['name'] == name:
            students.remove(i)
            print(students)
        else:
            print('你要删除的学员信息不存在')
else:
    print('输入错误, 请重新输入要操作的编号')

```