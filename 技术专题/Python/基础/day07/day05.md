# 函数的进阶

### 函数的递归

斐波那契
```python
def f(n):
    if n == 1 or n == 2:
        return 1
    return f(n - 1) + f(n - 2)

print(f(15))
```

n的阶乘
```python
def f(n):
    if n <= 2:
        return n
    return f(n - 1) * n

f(100)
```

猴子吃桃
```python
def f(n):
    if n == 10:
        return 1
    return (f(n + 1) + 1 ) * 2


print(f(1))
```