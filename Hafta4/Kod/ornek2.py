import time

# Seri - Sequential kod
def is_yap():
    print("is basladi")
    time.sleep(1)
    print("is bitti")

for _ in range(5):
    is_yap()