# 2x4 . 4x6 -> 2x6
# Matris boyutunu tanımlıyoruz
matrix_size = 3
# Matris a yı tanımlıyoruz.
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Matris b yi tanımlıyoruz.
matrix_b = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Boş bir matris tanımlıyoruz
result = [[0] * matrix_size for i in range(matrix_size)]
# Boş matrise matris çarpım değerlerini atamak için gerekli döngüler
for row in range(matrix_size):
    for col in range(matrix_size):
        for i in range(matrix_size):
            result[row][col] += matrix_a[row][i] * matrix_b[i][col]
# Matris satırlarını yazdırıyoruz
for row in range(matrix_size):
    print(matrix_a[row], matrix_b[row], result[row])



