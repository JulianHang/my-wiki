# with语句

python提供了with语句的这种写法, 既简单又安全, 并且with语句执行完成以后自动调用关闭文件操作, 即使出现异常也会自动调用关闭文件操作。

常规写法
```python
try:
    file = open("1.txt", 'r')
    file.write('abc')
except Exception as e:
    print(e)
finally:
    print('over')
    file.close()
```

with语句
```python
with open('1.txt', 'r') as file:
    file_data = file.read()
    print(file_data)
```