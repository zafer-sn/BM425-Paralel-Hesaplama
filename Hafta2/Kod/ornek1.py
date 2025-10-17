"""from collections import deque
liste2 = [2, 25, "test", 2.718]
liste2_deq = deque(liste2)
liste2_deq.popleft()"""


liste1 = [11, 3.14, "Zafer", True]
liste1[0] = 35
liste1.append(55)
liste1.append(1)
print(liste1.count(1))
print(True * 5)
liste1.insert(2, "deneme")
print(len(liste1))
liste1.pop(0)
del liste1[0]
print(*liste1)

liste3 = [-100, -5, 25, 55, 85]
liste3.sort()
liste3.reverse()
print(liste3)
print(5 not in liste3)

