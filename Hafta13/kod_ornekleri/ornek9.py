import time
from multiprocessing import Pipe, Process


def ping(pipe):
    while True:
        pipe.send(["ping", time.time()])
        txt = pipe.recv()
        print(txt)
        time.sleep(1)
def pong(pipe):
    while True:
        txt = pipe.recv()
        print(txt)
        time.sleep(1)
        pipe.send(["pong", time.time()])

if __name__ == '__main__':
    pipe_conn_a, pipe_conn_b = Pipe()
    p1 = Process(target=ping, args=(pipe_conn_a, ))
    p2 = Process(target=pong, args=(pipe_conn_b, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()




