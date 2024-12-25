# 2x4 . 4x6 -> 2x6
import os
import time
from random import Random
from threading import Thread, Barrier


matrix_size = 200
matrix_a = [[0] * matrix_size for a in range(matrix_size)]
matrix_b = [[0] * matrix_size for b in range(matrix_size)]
result = [[0] * matrix_size for i in range(matrix_size)]
r = Random()

b1 = Barrier(matrix_size + 1)
b2 = Barrier(matrix_size + 1)


def random_matrix_generator(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row][col] = r.randint(-10, 10)
def calculate_matrix(row):
    while True:
        b1.wait()
        for col in range(matrix_size):
            for i in range(matrix_size):
                result[row][col] += matrix_a[row][i] * matrix_b[i][col]
        b2.wait()

for row in range(matrix_size):
    Thread(target=calculate_matrix, args=(row, )).start()

start = time.time()
for t in range(10):
    random_matrix_generator(matrix_a)
    random_matrix_generator(matrix_b)
    result = [[0] * matrix_size for i in range(matrix_size)]
    b1.wait()
    b2.wait()

print(f"Geçen süre: {time.time()-start}")


