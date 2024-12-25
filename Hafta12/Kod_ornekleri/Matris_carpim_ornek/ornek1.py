# Basit matris çarpım örneği
# Matrisleri tanımlayalım
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

# Sonuç matrisini oluştur
# Sonuç matrisinin boyutları A'nın satır sayısı x B'nin sütun sayısı kadar olacak
result = [
    [0, 0],
    [0, 0]
]

# Matris çarpımını yapalım
for i in range(len(A)):  # A matrisinin satırları
    for j in range(len(B[0])):  # B matrisinin sütunları
        for k in range(len(B)):  # A matrisinin sütunları ve B matrisinin satırları
            result[i][j] += A[i][k] * B[k][j]

# Sonuçları yazdıralım
for row in result:
    print(row)
