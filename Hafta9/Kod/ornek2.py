import threading

sem = threading.Semaphore(1)

try:
    sem.acquire()
    print('Girdi')
    x = 1 / 0 # Hata oluşturur (ZeroDivisionError)
    sem.release()
except ZeroDivisionError:
    print('Hata oluştu')

# Buradaki soru: sem.acquire() yapılmıştı, release() oldu mu?
print(f'Semafor Değeri: {sem._value}')
