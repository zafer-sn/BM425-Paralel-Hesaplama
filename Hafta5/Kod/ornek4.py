import json
import string
from threading import Thread
import time
import urllib.request
from http.client import HTTPResponse

def istek_at(url, harf_sozlugu):
    cevap : HTTPResponse = urllib.request.urlopen(url)
    txt = cevap.read().decode("utf-8")
    for h in txt:
        karakter = h.lower()
        if karakter in harf_sozlugu:
            harf_sozlugu[karakter] += 1

baslangic_zamani = time.time()
harf_sozlugu = {k:0 for k in string.ascii_lowercase}
thread_listesi = []
for i in range(2000, 2021):
    t = Thread(target=istek_at, args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", harf_sozlugu))
    thread_listesi.append(t)
    
for j in thread_listesi:
    j.start()
for j in thread_listesi:
    j.join()
"""for k in string.ascii_lowercase:
    harf_sozlugu[k] = 0"""
#liste = [i for i in range(100)]
#print(string.ascii_lowercase)
print(json.dumps(harf_sozlugu, indent=4))
bitis_zamani = time.time()
print(f"Gecen sure: {bitis_zamani-baslangic_zamani}")
