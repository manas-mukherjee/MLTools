def is_palindrom(num):
    i = 0
    j = len(str(num)) - 1
    n = str(num)

    while i <= j:
        if n[i] != n[j]:
            return False
        i += 1
        j -= 1

    return True

# output = is_palindrom(997799)
# print(output)

def largest_palindrome():
    large_i = large_j = largest = 0

    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            num = i*j
            if is_palindrom(num):
                if num > largest:
                    largest = num
                    large_i = i
                    large_j = j
    return large_i, large_j

i, j = largest_palindrome()
print(i, j, i*j)
