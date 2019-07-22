import math

# comparison of different methods of calculating fibonacci numbers

def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# slows down after around n=30
def fibonacci_recursive(n):
    if n < 2:
        return n
    elif n < 3:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# in python, only accurate to around n=75, after that floating point errors cause inaccuracies
sqrt5 = math.sqrt(5)
phi = (1 + sqrt5) / 2
psi = (1 - sqrt5) / 2
def fibonacci_binet(n):
    fib = int((phi ** n - psi ** n) / sqrt5)
    return fib





def display_fib(i):
    fib_i = fibonacci_iterative(i)

    fib_r = fibonacci_recursive(i)

    fib_b = fibonacci_binet(i)

    print(f"{i:3}: {fib_i:10} {fib_r:12} {fib_b:14}")



print("  n    Iterative   Recursive    Binet's Formula")
print("-----------------------------------------------")
display_fib(10)
display_fib(20)
display_fib(30)
display_fib(40)
