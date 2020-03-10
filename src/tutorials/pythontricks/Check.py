def vowel_counter(data):
    cnt = 0
    for c in data:
        if c in 'aeiouAEIOU':
            cnt = cnt + 1
    return cnt
