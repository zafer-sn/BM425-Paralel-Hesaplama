import time
import queue
from threading import Thread
def consumer(qq):
    while True:
        txt = qq.get()
        print(txt)
        time.sleep(1)

def producer(qq):
    while True:
        qq.put("selam")
        print("Mesaj gönderildi!")
        time.sleep(1)

qq = queue.Queue()
t1 = Thread(target=consumer, args=(qq, ))
t2 = Thread(target=producer, args=(qq, ))
t1.start()
t2.start()
t1.join()
t2.join()

