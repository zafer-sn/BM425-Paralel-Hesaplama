# 2x4 . 4x6 -> 2x6
import time
from random import Random

matrix_size = 100
matrix_a = [[0] * matrix_size for a in range(matrix_size)]
matrix_b = [[0] * matrix_size for b in range(matrix_size)]
result = [[0] * matrix_size for i in range(matrix_size)]
r = Random()


def random_matrix_generator(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row][col] = r.randint(-10, 10)

random_matrix_generator(matrix_a)
random_matrix_generator(matrix_b)

start = time.time()
for t in range(10):
    for row in range(matrix_size):
        for col in range(matrix_size):
            for i in range(matrix_size):
                result[row][col] += matrix_a[row][i] * matrix_b[i][col]
print(f"Geçen süre: {time.time()-start}")


