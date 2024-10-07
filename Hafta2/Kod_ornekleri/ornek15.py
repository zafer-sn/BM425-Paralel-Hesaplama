fib = [1 ,1]
for i in range(10):
    fib.append(fib[-1] + fib[-2])
print(*fib)