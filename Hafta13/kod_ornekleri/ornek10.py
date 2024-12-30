from threading import Thread, Lock


def blue_robot(mtx1, mtx2):
    while True:
        mtx1.acquire()
        print("Blue robot mtx1'e erişti")
        mtx2.acquire()
        print("Blue robot mtx2'e erişti")
        mtx2.release()
        print("Blue robot mtx2'yi bıraktı")
        mtx1.release()
        print("Blue robot mtx1'yi bıraktı")
        print("Blue robot tüm mutexleri bıraktı")


def red_robot(mtx1, mtx2):
    while True:
        mtx2.acquire()
        print("Red robot mtx2'e erişti")
        mtx1.acquire()
        print("Red robot mtx1'e erişti")
        mtx1.release()
        print("Red robot mtx1'yi bıraktı")
        mtx2.release()
        print("Red robot mtx2'yi bıraktı")
        print("Red robot tüm mutexleri bıraktı")

mtx1 = Lock()
mtx2 = Lock()
t1 = Thread(target=blue_robot, args=(mtx1, mtx2))
t2 = Thread(target=red_robot, args=(mtx1, mtx2))
t1.start()
t2.start()
t1.join()
t2.join()