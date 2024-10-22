from threading import Thread

i = 0
def is_yap():
    print("İş başladı")
    global i
    print(i)
    for j in range(20000000):
        i += 1
    print("İş bitti")

for i in range(8):
    thr1 = Thread(target=is_yap)
    thr1.start()