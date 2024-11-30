from multiprocessing import Process


def asal_bul(sayi):
    asalmi = True
    for i in range(2, sayi):
        if sayi % i == 0:
            asalmi = False
            break
    return asalmi

def fonk1():
    for i in range(2, 51):
        if asal_bul(i) and asal_bul((2**i)-1):
            print(i)

def fonk2():
    for i in range(51, 101):
        if asal_bul(i) and asal_bul((2**i)-1):
            print(i)

if __name__ == '__main__':
    p1 = Process(target=fonk1)
    p2 = Process(target=fonk2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
