# 2x4 . 4x6 -> 2x6
from random import Random
matrix_size = 3
# Bütün matrisleri başlangıçta 0 elemanlarından oluşacak şekilde tanımlıyoruz
matrix_a = [[0] * matrix_size for a in range(matrix_size)]
matrix_b = [[0] * matrix_size for b in range(matrix_size)]
result = [[0] * matrix_size for i in range(matrix_size)]
# Rastgele değer üretmek için Random classından bir nesne üretip r ile referans ediyoruz
r = Random()

# Matrislere rastgele değerler atamak için yazdığımız fonksiyon
def random_matrix_generator(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row][col] = r.randint(-10, 10)
# Matrislere rastgele değerler atıyoruz
random_matrix_generator(matrix_a)
random_matrix_generator(matrix_b)
# Boş matrislere matris çarpım değerlerini atamak için gerekli döngüler

for row in range(matrix_size):
    for col in range(matrix_size):
        for i in range(matrix_size):
            result[row][col] += matrix_a[row][i] * matrix_b[i][col]
# Matris satırlarını yazdırıyoruz
for row in range(matrix_size):
    print(matrix_a[row], matrix_b[row], result[row])



