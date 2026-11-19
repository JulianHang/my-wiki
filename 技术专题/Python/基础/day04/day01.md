# 作业回顾

有一个数字，不知道具体是多少，用3去除剩2，用5去除剩3，用7去除剩2，问整个数是多少？1~100以内的整数

```python
i = 1
while i <= 100:
    if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
        print(i)
        break
    i += 1

```

```python
for i in range(1, 101):
    if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
        print(i)

```




报数字7：一些同学从1开始报数，当需要报出的数字尾数是7或者该数字是7的倍数时，则该同学跳过这个数字，不进行报数，所有同学都参与游戏后，游戏结束。如输入学生数量为50，游戏结束后，报数的同学数量为39

```python
studentcount = int(input('请输入学生的数量：'))
i = 1
sum = 0 
while i <= studentcount:
    if i % 10 == 7 or i  % 7 == 0 :
        i += 1
        continue
    print(i)
    i += 1
    sum += 1
    


```