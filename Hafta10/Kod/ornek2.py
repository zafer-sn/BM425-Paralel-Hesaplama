from concurrent.futures import ThreadPoolExecutor
import time
import threading

def gorev_yap(is_no, gorev_no):
    # Hangi Thread'in çalıştığını görelim
    thread_adi = threading.current_thread().name
    print(f"[{thread_adi}] Görev {is_no} başladı..., {gorev_no}")
    time.sleep(1) # İşlem simülasyonu
    return f"Görev {is_no} Bitti"

def selamla():
    print("Selam")

# Havuz oluşturuluyor (Maksimum 2 İşçi)
print("--- Havuz Açılıyor (Sadece 2 İşçi Var) ---")
# alias
with ThreadPoolExecutor(max_workers=2) as havuz:
    # 5 adet görevi havuza gönderiyoruz
    # map fonksiyonu, for döngüsü gibi çalışır ve işleri dağıtır
    sonuclar = havuz.map(gorev_yap, [1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
    havuz.submit(selamla)

print("--- Tüm İşler Tamamlandı ---")
