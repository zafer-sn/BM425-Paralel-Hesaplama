kume = {2, 2, 2, "selam", "selam", 5.6, False}
kume2 = {2, 3.14 , "deneme", 0}
try:
    kume.remove(11)
except KeyError as e:
    print("hata")
    print(e)
kume3 = kume.difference(kume2)
kume4 = kume.union(kume2)
print(*kume3)
print(*kume4)