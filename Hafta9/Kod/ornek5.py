import threading
import time

# Başlangıçta 0 (Kırmızı Işık)
start_sinyali = threading.Semaphore(0)

def kosucu():
    print("Koşucu: Tabanca sesini bekliyor (acquire)...")
    start_sinyali.acquire() # Sayaç 0 olduğu için burada bloklanır
    print("Koşucu: Sesi duydu, KOŞUYOR!")

def hakem():
    print("Hakem: Hazırlanıyor...")
    time.sleep(2)
    print("Hakem: ATEŞLEDİ! (release)")
    start_sinyali.release() # Sayacı 1 yapar, koşucuyu uyandırır

t1 = threading.Thread(target=kosucu)
t2 = threading.Thread(target=hakem)

t1.start()
t2.start()
