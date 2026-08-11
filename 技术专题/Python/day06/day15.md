# 把函数的返回值作为另外一个函数的参数

```python
def test1():
    return 50

def test2(num):
    print(num)

result = test1()
test2(result)
```