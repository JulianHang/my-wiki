### 逻辑运算符

| 运算符 | 描述 | 示例                                |
|-----|----|-----------------------------------|
| and | 与  | |
| or  | 或  ||
| not | 非  | |
```python
# 女孩子要求比较高，要求男孩子必须要有房且有车
# 表达式1 and 表达式2
# 有房 and 有车 则 牵手成功
# 有房 and 没车 则 牵手失败
# 无房 and 有车 则 牵手失败

# 女孩子要求一般，要求男孩子有房或者有车即可
```
```python
a = 1
b = 2
c = 3
print((a > b) and (b > c)) # False
print((a > b) or (b > c)) # False
print(not (a > b)) # True
```

### 短路运算
在逻辑运算中，不一定逻辑运算符的两边都是纯表达式，也可以是数值类型的输
**Python中把0、空字符串、None看成False，其他数值和非空字符串都看成True**, 所以：

① 在计算 a and b 时，如果 a 是False，则根据与运算法则，整个结果必定为False, 因此返回 a；如果 a 是True，则整个计算结果必定取决于b，因此返回b

② 在计算 a or b 时，如果 a 是True，则根据或运算法则，整个结果必定为True，因此返回a；如果 a 是False，则整个计算结果必定取决于b，因此返回b

所以Python解释器在做布尔运算时，只要能提前确定计算结果，它就不会往后算了，直接返回结果

```python
print(3 and 4 and 5)  # 
print(5 and 6 or 7)
4 > 3 and print('hello world')

```
