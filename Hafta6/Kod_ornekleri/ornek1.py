import multiprocessing
from multiprocessing import Process
def is_yap():
    print("İş başladı")
    i = 0
    for _ in range(1000001):
        i += 1
    print("İş bitti")

if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    processler = []

    for i in range(8):
        prc = Process(target=is_yap)
        processler.append(prc)

    for j in processler:
        j.start()
