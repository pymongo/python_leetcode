"""
python的threading.Timer更像是js的setTimeout
如果想要setInterval的效果需要死循环内不断调用或者递归调用
由于死循环会阻塞线程，若线程还有别的任务会导致interval变大/不准确
定时器的句柄定义成全局变量，创建的定时器进程和实例不会因为递归调用而堆积
"""
from threading import Timer
import os


def print_aaaa():
    print('aaaa')
    global timer_a
    timer_a = Timer(1, print_aaaa)
    timer_a.start()


def print_bbbb():
    print('bbbb')
    global timer_b
    timer_b = Timer(1, print_bbbb)
    timer_b.start()


def stop():
    timer_a.cancel()
    timer_b.cancel()
    os._exit(1)


if __name__ == '__main__':
    timer_a: Timer = Timer(interval=1, function=print_aaaa)
    timer_b: Timer = Timer(interval=1, function=print_bbbb)
    print_aaaa()
    print_bbbb()
    t = Timer(4, stop)
    t.start()
