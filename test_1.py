# __author__: "Yu Dongyue"
# date: 2021/4/30
# 每个独立的线程有一个程序的入口、顺序执行序列和程序的出口。不能独立运行，必须已存在应用程序中，由应用程序提供多个线程进行控制
"""
每个线程都有自己的CPU寄存器，成为线程的上下文，上下文反应了线程上次运行该CUP寄存器的状态
指令指针和堆栈指针寄存器是线程上下文中两个重要的寄存器，线程总是在进程得到上下文控制的，这些地址都用于标志拥有线程的进程地址空间的内存
"""
import _thread
import time


def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (thread_name, time.ctime(time.time())))


# 创建两个线程
try:
    _thread.start_new_thread(print_time, ("Thread-1", 2,))
    _thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print('Error: 无法启动线程')
while 1:
    pass
