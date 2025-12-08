import threading

sem = threading.Semaphore(0)

print('Başla')
sem.acquire()
print('Bitti')
