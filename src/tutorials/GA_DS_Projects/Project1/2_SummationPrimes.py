def is_prime(num):
    for i in range(2, num//2):
        if num%i == 0:
            return False
    return True

print(sum([i for i in range(2000) if is_prime(i)]))
