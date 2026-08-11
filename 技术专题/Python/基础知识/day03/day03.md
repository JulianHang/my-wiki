# 循环
### while循环的基本语法
① 定义一个计数器：i = 0
② 编写while循环结构
while 循环条件（判断计数器是否达到了目标位置）
    循环体1
    循环体2
    ③ 在循环内部更新计数器
    i = i + 1 或 i += 1

```python
i = 0
while i < 100:
    print('老婆大人我错了')
    i = i + 1


``` 

案例2：求1~100之间，所有偶数的和
```python
i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum = sum + i
    i += 1

print(f'所有偶数的和：{sum}')
```

### 两大关键词
break: 代表终止整个循环结构
continue： 代表中止当前循环，继续下一次循环

> break 关键字
```python
i = 1
while i <= 5:
    if i == 4:
        print('我已经吃饱了，实在吃不下了')
        break
    print(f'我正在吃第{i}个苹果 ')
    
    i = i + 1
```

> continue 关键字

```python
i = 1
while i <= 5:
    if i == 3:
        i += 1
        print('吃到了一只大虫子，这个苹果不吃了')
        continue
    print(f'正在吃第{i}个苹果')
    i += 1
```

### 案例
需求：计算机从1~10之间随机生成一个数字，然后 提示输入数字，如果我们输入的数字与随机数相等，则提示恭喜你，答对了。如果输入的数字比随机数大，则提示，猜大了。否则，则提示猜小了，一共有3次机会

```python
import random
i = 0
secretNum = random.randint(1, 10)

while i < 3:
    userNum = int(input('请输入您猜的数字：'))
    if secretNum == userNum:
        print('恭喜你，答对了')
        break
    elif secretNum > userNum:
        print('猜小了')
    else: 
        print('猜大了')
    i += 1
    
```

### 循环嵌套

编写一个简单的while循环结构。
```python
# 初始化计数器 
i = 0 或 i = 1
# 编写循环条件
while i < 边界值:
    循环体代码
    更新计数器
    i += 1

```
所谓的while嵌套循环就是在while循环的基础上，把循环体代码更换为一层while循环，就组成了while嵌套循环。
```python
# 第一步，初始化外层循环计数器
i = 1
# 第二步，编写外层循环的条件
while i <= 3:
    # 第四步，初始化内层循环计数器
    j = 1
    # 第五步，编写内层循环的条件
    while j <= 3:
        循环体代码
        # 第6步，更新内层循环计数器
        j += 1
    # 第三步，更新外层循环计数器
    i += 1
```