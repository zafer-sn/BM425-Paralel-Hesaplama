# Matris çarpım örneği - list comprehension ile
# Matrisleri tanımlayalım
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

# List comprehension ile matris çarpımını yapalım
result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

# Sonuçları yazdıralım
for row in result:
    print(row)
