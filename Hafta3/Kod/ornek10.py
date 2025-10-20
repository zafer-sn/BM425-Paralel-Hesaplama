def ikiye_bol(sayi):
    return sayi / 2

l = list(range(1, 151))
m = list(map(ikiye_bol, l))
print(m)