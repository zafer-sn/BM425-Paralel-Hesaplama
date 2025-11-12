"""
Resim indirme işleminin paralelleştirilmesi
requests modülü
os modülü
"""

import os
import time
import requests
DOWLOAD_FOLDER = "Hafta6/images"
def setup():
    if not os.path.exists(DOWLOAD_FOLDER):
        os.makedirs(DOWLOAD_FOLDER)
    
    for file in os.listdir(DOWLOAD_FOLDER):
        os.remove(os.path.join(DOWLOAD_FOLDER, file))

setup()

toplam_indirilen_resim = 0
toplam_indirilen_byte = 0

def resim_indir(id):
    global toplam_indirilen_resim, toplam_indirilen_byte
    response = requests.get("https://picsum.photos/200/300")
    full_path = os.path.join(DOWLOAD_FOLDER, f"image_{id}.jpg")
    with open(full_path, "wb") as file:
        file.write(response.content)

    mevcut_toplam_resim = toplam_indirilen_resim
    mevcut_toplam_byte = toplam_indirilen_byte
    # time.sleep(0.1)
    suanki_toplam_resim = mevcut_toplam_resim + 1
    suanki_toplam_byte = mevcut_toplam_byte + len(response.content)

    toplam_indirilen_resim = suanki_toplam_resim
    toplam_indirilen_byte = suanki_toplam_byte

baslangic_zamani = time.time()
for i in range(10):
    resim_indir(i)
bitis_zamani = time.time()

print(f"Toplam resim: {toplam_indirilen_resim}")
print(f"Toplam byte: {toplam_indirilen_byte}")
print(f"Gecen sure: {bitis_zamani-baslangic_zamani}")
