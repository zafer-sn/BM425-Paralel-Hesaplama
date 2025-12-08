import threading

# Kapasitesi 1 olan BoundedSemaphore
guvenli_semafor = threading.BoundedSemaphore(1)

def hatali_kod():
    guvenli_semafor.acquire()
    print("Kaynak alındı.")
    
    # İşlem bitti, bırakıyoruz
    guvenli_semafor.release()
    print("Kaynak bırakıldı (Sayaç: 1).")
    
    try:
        guvenli_semafor.release()
    except ValueError as e:
        print(f"HATA YAKALANDI: {e}")
        print("BoundedSemaphore, kapasite aşımına izin vermedi!")

t = threading.Thread(target=hatali_kod)
t.start()
