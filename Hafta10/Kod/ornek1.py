import threading
import time

def isci():
    print(f"Baslayan thread: {threading.current_thread()}")
    time.sleep(2)
    print(f"Biten thread: {threading.current_thread()}")

# 3 tane isimsiz, 1 tane isimli thread başlatalım
t1 = threading.Thread(target=isci)
t1.start()
t2 = threading.Thread(target=isci)
t2.start()
t3 = threading.Thread(target=isci, name="ÖZEL_THREAD_X")
t3.start()

print(f"Toplam Aktif Thread Sayısı: {threading.active_count()}")

print("\n--- Thread Listesi ---")
for t in threading.enumerate():
    print(f"Thread Adı: {t.name}, Canlı mı?: {t.is_alive()}")
