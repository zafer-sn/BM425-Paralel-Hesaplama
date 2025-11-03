from multiprocessing import Process
import time
import multiprocessing

def is_yap():
    print("is basladi")    
    i = 0
    for _ in range(2000000000):
        i+=1
    print("is bitti")

if __name__ == "__main__":
    baslangic_zamani = time.time()
    multiprocessing.set_start_method("spawn")
    process_listesi = []
    for _ in range(12):
        p = Process(target=is_yap, args=())
        process_listesi.append(p)

    for j in process_listesi:
        j.start()
    for j in process_listesi:
        j.join()
    bitis_zamani = time.time()
    print(f"Gecen sure: {bitis_zamani-baslangic_zamani}")
