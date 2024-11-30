import json
import string
import time
import urllib.request
from threading import Thread, Lock

biten_thread_sayisi = 0
def count_letter(l_dict, url, mtx):
    response = urllib.request.urlopen(url)
    r_txt = str(response.read().decode("utf-8"))
    # r_txt.replace(" ", "")
    # print(r_txt)
    for l in r_txt:
        letter = l.lower()
        if letter in l_dict:
            mtx.acquire()
            l_dict[letter] += 1
            mtx.release()
    mtx.acquire()
    global biten_thread_sayisi
    biten_thread_sayisi += 1
    mtx.release()

le_dict = {}
ing_harfler = string.ascii_lowercase

for i in ing_harfler:
    le_dict[i] = 0

mutex = Lock()

baslangic_zamani = time.time()
for i in range(1000, 1031):
    Thread(target=count_letter, args=(le_dict, f"https://www.rfc-editor.org/rfc/rfc{i}.txt", mutex)).start()
while True:
    mutex.acquire()

    if biten_thread_sayisi == 31:
        break
    mutex.release()

    time.sleep(0.5)
bitis_zamani = time.time()
print(json.dumps(le_dict, indent=4))
print(f"Geçen süre: {bitis_zamani-baslangic_zamani}")
