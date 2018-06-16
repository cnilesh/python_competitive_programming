def power(n, x):
    print('x', x)
    if x == 1:
        return n
    partial = power(n, x//2)
    if x%2 == 1:
        return n*partial*partial
    return partial*partial
print(power(5,7))