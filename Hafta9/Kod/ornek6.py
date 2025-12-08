import threading
import time

def arka_plan_servisi():
    sayac = 0
    while True:
        time.sleep(0.5)
        sayac += 1
        print(f"[Daemon] Arka planda çalışıyor... {sayac}")

# daemon=True demezsek bu döngü sonsuza kadar sürer, program kapanmaz.
# daemon=True dediğimiz için ana program bitince bu da ölecek.
t = threading.Thread(target=arka_plan_servisi, daemon=True)
t.start()

print("Ana Program: İşlem yapıyor (2 saniye sürecek)...")
time.sleep(2)
print("Ana Program: Bitti. Çıkış yapılıyor.")
# Program burada biter, Daemon thread'in mesajları kesilir.
