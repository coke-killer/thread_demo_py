# __author__: "Yu Dongyue"
# date: 2021/4/30
# 当多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步
"""
使用Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire和release方法，对于那些每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间。如下：
多线程的优势在于可以运行多个任务。但是当线程需要共享数据时，可能存在数据不同步的问题
考虑这样一种情况：线程“set”从后面把所有元素改成1，线程print负责从前向后读取列表并打印，可能set进程开始修改的时候，线程print便来打印列表了，输出就成了一半0一半1，这就是因为数据不同步的结果，为了避免这种情况发生，引入锁的概念
锁由两种状态--锁定和未锁定。每当一个线程比如set要访问共享数据时，必先获得锁定；如已经有别的线程比如print获得锁定，那么就让线程set暂停。也就是同步阻塞，等到线程peint访问完毕，释放锁以后，再让线程set继续
这样，打印列表要么全部输出0 要么全部输出1
"""
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程" + self.name)
        # 获取锁用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        threadLock.release()


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
