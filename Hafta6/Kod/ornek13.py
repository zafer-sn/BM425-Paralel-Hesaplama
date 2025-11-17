from threading import Thread
import requests
SERVER_URL = "http://127.0.0.1:5000/"
ISTEK_SAYISI = 50
requests.get(f"{SERVER_URL}/sifirla")
print("Ziyaretci sayisi sifirlandi!")
def istek_at():
    try:
        response = requests.get(SERVER_URL)
        if response.status_code == 200:
            print(f"İstek basarili: {response.json()['ziyaretci_sayisi']}")
    except Exception as e:
        print(e)

threadler = []
for _ in range(ISTEK_SAYISI):
    t = Thread(target=istek_at, args=())
    threadler.append(t)

for j in threadler:
    j.start()
for j in threadler:
    j.join()

son_deger = requests.get(SERVER_URL).json()['ziyaretci_sayisi']
print(son_deger)
print(ISTEK_SAYISI)