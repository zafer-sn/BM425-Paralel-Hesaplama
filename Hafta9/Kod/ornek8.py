import threading
import time

cikis_sinyali = threading.Event()

def dosya_isleyici():
    while not cikis_sinyali.is_set():
        print("İşçi: Dosya işleniyor...")
        time.sleep(1) # Uzun süren iş simülasyonu
    print("İşçi: Çıkış sinyali alındı. Temizlik yapıp kapanıyor. ")

t = threading.Thread(target=dosya_isleyici)
t.start()

time.sleep(3)
print("Ana Thread: Artık durmalısın.")
cikis_sinyali.set() # Bayrağı kaldır
