# while循环与for循环中的else结构

为什么需要在while循环中添加else结构
> 循环可以和else配合使用，else下方缩进的代码指的是当循环正常结束之后要执行的代码。强调：正常结束，非正常结束，其else中的代码是不会执行的，如遇到break的情况

```python
i = 0
while i < 5:
    print('老婆大人，我错了')
    i += 1
    
# 循环结束后，女朋友就原谅我了
else:
    print('女朋友原谅我了')

```

> break关键字对while ... else 结构的影响
```python
i = 0
while i < 5:
    if i == 3:
        print('这遍说的不够真诚')
        break
    print('老婆大人，我错了')
else:
    print('女朋友原谅我了')

# 不会执行 女朋友原谅我了
```
由运行结果可知，如果我们在while循环中，使用了break，一旦执行了break，else就不会执行

> continue关键字对while...else 结构的影响

在while循环中使用continue，else语句会正常执行


### for循环结构中的else结构
```python
# for i in 序列：
#     print('')
# else:
#     当for循环正常结束后，返回的代码

```
> break关键字对for...else结构的影响

同while一样

> continue关键字对for...else结构的影响

同while一样