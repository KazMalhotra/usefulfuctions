def isprime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    i = 7
    while i ** 2:
        if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
            return False
        if x % i == 0:
            return False
        i += 2
    return True
