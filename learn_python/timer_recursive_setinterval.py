"""
python的threading.Timer更像是js的setTimeout
如果想要setInterval的效果需要死循环内不断调用或者递归调用
由于死循环会阻塞线程，若线程还有别的任务会导致interval变大/不准确
定时器的句柄定义成全局变量，创建的定时器进程和实例不会因为递归调用而堆积
"""
from threading import Timer


class SetInterval:
    timer_1: Timer
    timer_2: Timer
    stop_timer_flag: bool = False

    @staticmethod
    def fn_1():
        print('Call fn_1')
        # threading.Timer约等于JS的setTimeout
        # 递归调用setTimeout可以实现setInterval
        SetInterval.timer_1 = Timer(interval=1, function=SetInterval.fn_1)
        SetInterval.timer_1.start()

    @staticmethod
    def fn_2():
        print('Call fn_2')
        SetInterval.timer_2 = Timer(interval=1, function=SetInterval.fn_2)
        SetInterval.timer_2.start()

    @staticmethod
    def stop_all():
        assert SetInterval.timer_1 is not None
        assert SetInterval.timer_2 is not None
        print("stop_all")
        # 在setTimeout的回调没被执行时，把timer关掉停掉递归调用setTimeout
        SetInterval.timer_1.cancel()
        SetInterval.timer_2.cancel()


if __name__ == '__main__':
    SetInterval.fn_1()
    SetInterval.fn_2()
    Timer(interval=4, function=SetInterval.stop_all).start()
