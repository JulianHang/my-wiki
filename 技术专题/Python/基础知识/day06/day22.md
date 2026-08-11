# 学员管理系统

```python

def menu():
    print('-' * 40)
    print('xx通讯录管理系统V1.0')
    print('1、添加学员信息')
    print('2、删除学员信息')
    print('3、修改学员信息')
    print('4、查询学员信息')
    print('5、遍历所有学员信息')
    print('6、退出系统')
    print('-' * 40)

    
info = []

def add_student():
    """添加学员"""
    info_dict = {}
    info_dict['name'] = input('请输入学员的姓名：')
    info_dict['age'] = input('请输入学员的年龄：')
    info_dict['mobile'] = input('请输入学员的电话：')
    global info
    info.append(info_dict)
    print('学员信息添加成功')
    print(info)

    
def del_student():
    """删除学员"""
    name = input('请输入你要删除的学员信息：')
    for i in info:
        if i['name'] == name:
            info.remove(i)
            print('删除学员信息成功')
            print(info)
            break
    else:
        print('暂未查询到学员信息')
        
        
def modify_student():
    name = input('请输入你要修改的学员信息：')
    for i in info:
        if i['name'] == name:
            i['name'] = input('请输入修改后的姓名：')
            i['age'] = input('请输入修改后的年龄：')
            i['mobile'] = input('请输入修改后的电话：')
            print('学员信息修改成功')
            print(info)
            break
    else:
        print('暂未查询到学员信息')    

        
def show_student():        
    name = input('请输入你要查询的学员信息：')
    for i in info:
        if i['name'] == name:
            print(f'姓名：{i["name"]}, 年龄：{i["age"]}, 电话：{i["mobile"]}')
            break
    else:
        print('暂未查询到学员信息')
        
        
def show_all():
    for i in info:
        print(f'姓名：{i["name"]}, 年龄：{i["age"]}, 电话：{i["mobile"]}')

while True:
    menu()
    
    user_num = int(input('请输入你要操作的功能序号：'))
    
    if user_num == 1:
        add_student()
    
    elif user_num == 2:
        del_student()
    
    elif user_num == 3:
        modify_student()
    
    elif user_num == 4:
        show_student()
        
    elif user_num == 5:
        show_all()
        
    elif user_num == 6:
        print('感谢你使用xx系统')
        break
    else:
        print('信息输入错误, 请重新输入...')

```