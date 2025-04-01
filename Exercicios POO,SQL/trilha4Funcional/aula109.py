def fatorial(x):
    return ((x * fatorial(x-1))if x > 1 else 1)

print(fatorial(5))