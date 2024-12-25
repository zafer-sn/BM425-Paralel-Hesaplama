# Basit matris çarpım örneği - numpy ile
import numpy as np

# Matrisleri numpy dizileri olarak tanımlayalım
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Numpy ile matris çarpımını yapalım
result = np.dot(A, B)

# Sonuçları yazdıralım
print(result)
