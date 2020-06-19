import threading
from time import sleep, strftime


def fn():
    print(f"thread[{threading.get_ident()}]: {strftime('%H:%M:%S')}")


class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()
        self.running = True

    def run(self):
        while self.running:
            fn()
            sleep(1)

    def stop(self):
        self.running = False


if __name__ == '__main__':
    t = threading.Thread(target=fn, name='threading.Thread')
    t.start()
    # t.join()
    mt = MyThread()
    mt.start()
    sleep(2)
    mt.stop()
