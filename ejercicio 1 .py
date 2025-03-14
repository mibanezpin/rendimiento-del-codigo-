import time

def fibonaccii(n):
    if n <= 1:
        return n
    return fibonaccii(n-1) + fibonaccii(n-2)

def fibonacci_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def factorial_rec(n):
    return 1 if n <= 1 else n * factorial_rec(n-1)

def factorial_iter(n):
    resultado = 1
    for i in range(2, n+1):
        resultado *= i
    return resultado

valores_n = [10, 20, 30, 40, 50]

for n in valores_n:
    print(f"n = {n}")
    
    inicio = time.time()
    try:
        fibonaccii(n)
    except RecursionError:
        print("Fibonacci recursivo falló")
    print(f"Fibonacci recursivo: {time.time() - inicio:.5f}s")
    
    inicio = time.time()
    fibonacci_iter(n)
    print(f"Fibonacci iterativo: {time.time() - inicio:.5f}s")
    
    inicio = time.time()
    factorial_rec(n)
    print(f"Factorial recursivo: {time.time() - inicio:.5f}s")
    
    inicio = time.time()
    factorial_iter(n)
    print(f"Factorial iterativo: {time.time() - inicio:.5f}s")
    
    print("-")
