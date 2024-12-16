from threading import Thread
# Thread ile yapılan örnekte değer değişir!
sayi = 0
def hesapla():
    global sayi
    for i in range(100):
        sayi += i

t1 = Thread(target=hesapla)
t1.start()
t1.join()
print(sayi)