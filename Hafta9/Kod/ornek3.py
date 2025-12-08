import threading
import time
import random
# Otopark kapasitesi: 4 Araç
otopark_semaforu = threading.Semaphore(7)

def arabayi_park_et(arac_no):
    print(f"Araç {arac_no} kapıya geldi, yer bekliyor...")
    
    with otopark_semaforu:
        print(f"{arac_no} PARK ETTİ. (İçerideki araç sayısı artıyor)")
        time.sleep(random.randint(1, 3)) # Park süresi
        print(f"{arac_no} ÇIKIŞ YAPTI.")

threadler = []
for i in range(1, 11):
    t = threading.Thread(target=arabayi_park_et, args=(i,))
    threadler.append(t)
    t.start()
