from multiprocessing import Process
# Process ile yapılan örnekte değer değişmez!
sayi = 0
def hesapla():
    global sayi
    for i in range(100):
        sayi += i
if __name__ == '__main__':
    t1 = Process(target=hesapla)
    t1.start()
    t1.join()
    print(sayi)