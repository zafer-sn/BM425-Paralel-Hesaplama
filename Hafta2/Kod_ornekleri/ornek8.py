liste = ["merhaba", 2, True, 3.14]
liste[0] = "selam"
"""for i in dir(list):
    if "__" not in i:
        print(i)"""
liste.append(5)
liste.pop(0)

liste.remove(2)
liste.insert(2, "deneme")
liste.clear()
# immutable
# mutable
print(*liste)
"""liste2 = list(["slm", 3, False])
print(*liste2)"""