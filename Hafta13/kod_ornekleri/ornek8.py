import time
from multiprocessing import Process, Queue, Pipe
# from threading import Thread


def consumer(pipe_conn_a):
    while True:
        txt = pipe_conn_a.recv() # receive -> almak
        print(txt)
        time.sleep(1)

def producer(pipe_conn_b):
    while True:
        pipe_conn_b.send("selam")
        print("Mesaj gönderildi!")
        time.sleep(1)
if __name__ == '__main__':
    # qq = Queue(maxsize=10)
    pipe_conn_a, pipe_conn_b = Pipe()
    p1 = Process(target=consumer, args=(pipe_conn_b, ))
    p2 = Process(target=producer, args=(pipe_conn_a, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Sonlandı")

