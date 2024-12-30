import time
import queue
from threading import Thread
def consumer(qq):
    txt = qq.get()
    print(txt)
    time.sleep(1)

def producer(qq):
    qq.put(["merhaba", 3.14, -5, False])
    print("Mesaj gönderildi!")
    time.sleep(1)

qq = queue.Queue()
t1 = Thread(target=consumer, args=(qq, ))
t2 = Thread(target=producer, args=(qq, ))
t1.start()
t2.start()
t1.join()
t2.join()

