"""
Dosya arama örneği
"""
import os
import time

eslesmeler = []
def dosya_arama(root, keyword):
    global eslesmeler
    print(f"{root} klasöründe araniyor...")
    for file in os.listdir(root):
        full_path = os.path.join(root, file)
        if keyword in file:
            eslesmeler.append(full_path)
        if os.path.isdir(full_path):
            dosya_arama(full_path,keyword)

baslangic_zamani = time.time()
dosya_arama("E:/08.06.2024 3DVAEGAN/3DVAEGAN", "1eb3af39d93c8bf2ddea2f4a0e0f0d2e_002.png")
print("-------------------------------------------------------")
for i in eslesmeler:
    print(f"Bulunan: {i}")
bitis_zamani = time.time()
print(f"Gecen sure: {bitis_zamani-baslangic_zamani}")