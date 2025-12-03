def fib(n):
    if n == 0 or n == 1:
        return n
    grandparent = 0
    parent = 1
    current = None
    for i in range(1, n):
        current = grandparent + parent
        grandparent = parent
        parent = current

    return current