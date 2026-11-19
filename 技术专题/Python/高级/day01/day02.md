from msilib import add_stream

# 线程

### 导入线程模块

```python
import threading
```

- group：线程组, 目前只能使用None
- target：执行的目标任务名
- args：以元组的方式给执行任务传参
- kwargs：以字典方式给执行任务传参
- name：线程名, 一般不用设置

### 启动线程
启动线程使用start方法

### 多线程完成多任务的代码
```python
import threading
import time

def sing():
    current_thread = threading.current_thread()
    print('sing:', current_thread)
    for i in range(3):
        print('唱歌中')
        time.sleep(0.2)
        
def dance():
    current_thread = threading.current_thread()
    print('dance:', current_thread)
    for i in range(3):
        print('跳舞中')
        time.sleep(0.2)

if __name__ == '__main__':
    current_thread = threading.current_thread()
    print('main_thread:', current_thread)

    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)
    
    sing_thread.start()
    dance_thread.start()
```

### 线程执行带有参数的任务
```python
import threading

def show_info(name, age):
    print('name:', name, age)
    
if __name__ == '__main__':
    # sub_thread = threading.Thread(target=show_info, args=('lisi', 20))
    sub_thread = threading.Thread(target=show_info, kwargs={"name": '王五', 'age': 20})

    sub_thread.start()
```

### 线程的注意点
- 线程之间执行是无序的
- 主线程会等待所有的子进程执行结束在结束
- 线程之间共享全局变量
- 线程之间共享全局变量数据出现问题


线程之间执行是无序的
```python
import threading
import time

def task():
    time.sleep(1)
    print(threading.current_thread())

if __name__ == '__main__':
    for i in range(20):
        sub_thread = threading.Thread(target=task)
        sub_thread.start()
```

线程之间共享全局变量
```python
import threading
import time

g_list = []

def add_data():
    for i in range(3):
        g_list.append(i)
        print('add：', i)
        time.sleep(0.2)

    print('添加数据完成：', g_list)

def read_data():
    print(g_list)

if __name__ == '__main__':
    add_thread = threading.Thread(target=add_data)
    read_thread = threading.Thread(target=read_data)

    add_thread.start()
    # 让当前线程(主线程)等待添加数据的子线程执行完成以后代码在继续执行
    add_thread.join()
    read_thread.start()
```


线程之间共享全局变量数据出现问题
```python
import threading

g_num = 0

def task1():
    for i in range(10000000):
        # 每循环一次给全局变量加1
        global g_num  # 表示要声明修改全局变量的内存地址
        g_num = g_num + 1

    print('task1:', g_num)


def task2():
    for i in range(10000000):
        # 每循环一次给全局变量加1
        global g_num  # 表示要声明修改全局变量的内存地址
        g_num = g_num + 1

    print('task2:', g_num)

if __name__ == '__main__':
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)

    first_thread.start()
    first_thread.join()
    second_thread.start()
```

互斥锁
```python
import threading

g_num = 0

# 创建互斥锁, Lock本质上是一个函数, 通过调用函数可以创建一个互斥锁
lock = threading.Lock()

def task1():
    lock.acquire()
    for i in range(1000000):
        # 每循环一次给全局变量加1
        global g_num  # 表示要声明修改全局变量的内存地址
        g_num = g_num + 1

    print('task1:', g_num)
    lock.release()


def task2():
    lock.acquire()
    for i in range(1000000):
        # 每循环一次给全局变量加1
        global g_num  # 表示要声明修改全局变量的内存地址
        g_num = g_num + 1

    print('task2:', g_num)
    lock.release()

if __name__ == '__main__':
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)

    first_thread.start()
    second_thread.start()

    # 互斥锁可以保证同一时刻只有一个线程去执行代码, 能够保证全局变量的数据没有问题
    # 线程等待和互斥锁都是把多任务改成单任务去执行, 保证了数据的准确性, 但是执行性能会下降
```

