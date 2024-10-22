import time
from threading import Thread
def selamla():
    print("Selam")
    time.sleep(1)
    print("Gorusuruz")
for i in range(5):
    thr1 = Thread(target=selamla) # Thread thr1 = new Thread();
    thr1.start()