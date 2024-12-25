# 2x4 . 4x6 -> 2x6
import multiprocessing
import os
import time
from random import Random
from multiprocessing import Process, Barrier
# Matris oluşturma basit kodları
matrix_size = 200
process_count = 8

r = Random()


# multiprocessing.Array("i" [1, 2 ,3][2])
def random_matrix_generator(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row * matrix_size + col] = r.randint(-10, 10)
def calculate_matrix(id, matrix_a, matrix_b, result, b1, b2):
    while True:
        b1.wait()
        for row in range(id,matrix_size, process_count):
            for col in range(matrix_size):
                for i in range(matrix_size):
                    result[row * matrix_size + col] += matrix_a[row * matrix_size + i] * matrix_b[i * matrix_size + col]
        b2.wait()

if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    b1 = Barrier(process_count + 1)
    b2 = Barrier(process_count + 1)

    """matrix_a = [[0] * matrix_size for a in range(matrix_size)]
    matrix_b = [[0] * matrix_size for b in range(matrix_size)]
    result = [[0] * matrix_size for i in range(matrix_size)]"""
    # [0]* 10
    matrix_a = multiprocessing.Array("i", [0] * (matrix_size*matrix_size), lock=False)
    matrix_b = multiprocessing.Array("i", [0] * (matrix_size*matrix_size), lock=False)
    result = multiprocessing.Array("i", [0] * (matrix_size*matrix_size), lock=False)

    for pr in range(process_count):
        Process(target=calculate_matrix, args=(pr, matrix_a, matrix_b, result, b1, b2)).start()

    start = time.time()
    for t in range(10):
        random_matrix_generator(matrix_a)
        random_matrix_generator(matrix_b)
        for i in range(matrix_size * matrix_size):
            result[i] = 0
        b1.wait()
        b2.wait()

    print(f"Geçen süre: {time.time()-start}")


