import time
from multiprocessing import Process


def asal_sayi_bul(sayi):
    asalmi = True
    for i in range(2, sayi):
        if sayi % i == 0:
            asalmi = False
            break
    return asalmi


def bul1():
    for i in range(2, 25001):
        asal_sayi_bul(i)

def bul2():
    for i in range(25001, 50001):
        asal_sayi_bul(i)

def bul3():
    for i in range(50001, 75001):
        asal_sayi_bul(i)

def bul4():
    for i in range(75001, 100001):
        asal_sayi_bul(i)


if __name__ == '__main__':
    processler = []
    bas_zamani = time.time()
    prcs1 = Process(target=bul1)
    prcs2 = Process(target=bul2)
    prcs3 = Process(target=bul3)
    prcs4 = Process(target=bul4)
    prcs1.start()
    prcs2.start()
    prcs3.start()
    prcs4.start()
    prcs1.join()
    prcs2.join()
    prcs3.join()
    prcs4.join()
    bit_zamani = time.time()
    print(f"Geçen süre: {bit_zamani-bas_zamani}")

