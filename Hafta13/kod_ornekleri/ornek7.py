import time
from multiprocessing import Process, Queue
# from threading import Thread


def consumer(qq):
    while True:
        txt = qq.get()
        print(txt)
        time.sleep(1)

def producer(qq):
    while True:
        qq.put("selam")
        print("Mesaj gönderildi!")
        # time.sleep(1)
if __name__ == '__main__':
    qq = Queue(maxsize=10)
    p1 = Process(target=consumer, args=(qq, ))
    p2 = Process(target=producer, args=(qq, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Sonlandı")

