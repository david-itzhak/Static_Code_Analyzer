def fibonacci(n):
    current_int = 0
    next_int = 1
    for _ in range(n):
        yield current_int
        current_int, next_int = next_int, next_int + current_int
