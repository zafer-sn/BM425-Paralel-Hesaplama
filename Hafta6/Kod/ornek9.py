import os
from threading import Thread
import time

eslesmeler = []
def dosya_arama(root, keyword):
    global eslesmeler
    print(f"{root} klasöründe araniyor...")
    threadler = []
    for file in os.listdir(root):
        full_path = os.path.join(root, file)
        if keyword in file:
            eslesmeler.append(full_path)
        if os.path.isdir(full_path):
            t = Thread(target=dosya_arama, args=(full_path,keyword))
            t.start()
            threadler.append(t)
    for j in threadler:
        j.join()

baslangic_zamani = time.time()
t = Thread(target=dosya_arama, args=("E:/08.06.2024 3DVAEGAN/3DVAEGAN", "1eb3af39d93c8bf2ddea2f4a0e0f0d2e_002.png"))
t.start()
t.join()
print("-------------------------------------------------------")
for i in eslesmeler:
    print(f"Bulunan: {i}")
bitis_zamani = time.time()
print(f"Gecen sure: {bitis_zamani-baslangic_zamani}")