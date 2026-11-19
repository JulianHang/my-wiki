# Python数据类型转换

```python
# 使用Python实现超市的收银系统
name = input('请输入你要购买商品的名称：')
id = input('请输入你要购买的商品编号：')
price = input('请输入你要购买的商品价格：')
print(f'您购买了{name}，商品编号为{id}，商品价格为{price}，欢迎下次光临')

print('-' * 10)
```

```python
# 案例1：把用户输入的幸运数字，转换为整型
num = input('请输入你的幸运数字：')
print(type(num))

print('-' * 20)
num = int(num)
print(type(num))

# 案例2：多种数据类型转换
# int -> float
num1 = 10
print(type(num1))
print(type(float(num1)))

print('-' * 20)
# float -> int   其小数点的位数会丢失
num2 = 18.88
print(int(num2))

# str -> float/int
str1 = '20'
str2 = '10.88'
print(type(int(str1)))
print(type(float(str2)))


# eval方法的使用，把字符串的数字转换为原数据类型
price = input('请输入你购买商品的价格')
print(eval(price))
print(type(eval(price)))  # int/float
# str1 = '10'  经过eval(str1) 转换，转换为int类型
# str2 = '10.88' 经过eval(str1) 转换，转换为float类型

```

### 总结
int(): 转整型
float(): 转浮点类型
str(): 转字符串类型
eval(): 把字符串转换为原数据类型
但是要特别注意，当float浮点类型转换为int整型时，其小数点后面位数会丢失