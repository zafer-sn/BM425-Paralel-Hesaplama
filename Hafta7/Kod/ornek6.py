from threading import Condition, Thread


sira = "ping"
cv = Condition()

def ping():
    global sira
    for _ in range(4):
        with cv:
            while sira != "ping":
                cv.wait()
            print("PING")
            sira = "pong"
            cv.notify()

def pong():
    global sira
    for _ in range(3):
        with cv:
            while sira != "pong":
                cv.wait()
            print("PONG")
            sira = "ping"
            cv.notify()

t1 = Thread(target=ping, args=())
t2= Thread(target=pong, args=())
t1.start()
t2.start()
t1.join()
t2.join()