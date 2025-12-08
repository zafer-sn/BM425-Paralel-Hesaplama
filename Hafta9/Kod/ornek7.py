import threading
import time

def arka_plan():
    time.sleep(2)
    print('Arka Plan Bitti')

# daemon=True olarak ayarlandı
t = threading.Thread(target=arka_plan, daemon=True)
t.start()
time.sleep(2)
print('Ana Program Bitti')
