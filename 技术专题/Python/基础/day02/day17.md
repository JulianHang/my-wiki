# 综合案例：石头剪刀布
1、需求分析：
参与游戏的角色有两个（玩家与电脑），玩家手工出拳，电脑随机出拳，根据石头剪刀布判断输赢。

玩家：player
电脑：computer

输赢结果很重要，有三种情况：

① 玩家赢
player: 石头 赢computer: 剪刀
player: 剪刀 赢computer: 布
player: 布 赢computer: 石头

② 平局
只要player与computer出拳相等，就代表平局

③电脑赢
如果不满足以上两个条件，则电脑获胜

```python
player = int(input("请输入你的出拳"))
computer = 1
    
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print('玩家获胜')
elif player == computer:
    print('平局')
else:
    print('电脑获胜')

```

### 随机出拳
Python语法非常的强大，强大之处在于其拥有很多模块，这些模块中拥有很多别人已经开发好的代码，我们可以直接导入到我们的程序中即可使用。
随机出拳其实就是随机从0，1，2中选出一个数字。

① import导入模块
② 使用模块中的方法

```python
import random

# 调用内部封装的方法
computer = random.randint(0, 2)

```