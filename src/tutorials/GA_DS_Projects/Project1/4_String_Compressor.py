def string_composer(input_string, is_case_sensitive=True):
    if not input_string:
        return ''

    if not is_case_sensitive:
        input_string = input_string.lower()

    run_length_encoded_str = []

    char_val = input_string[0]
    char_count = 1

    for ind, c in enumerate(input_string[:-1]):

        if input_string[ind+1] == char_val:
            char_count += 1
        else:
            run_length_encoded_str.append(char_val)
            run_length_encoded_str.append(str(char_count))
            char_val = input_string[ind + 1]
            char_count = 1
    run_length_encoded_str.append(char_val)
    run_length_encoded_str.append(str(char_count))

    encoded_str = ''.join(run_length_encoded_str)
    return input_string if len(encoded_str) > len(input_string) else encoded_str


print(string_composer('aabcccccaaa'))
print(string_composer('aaaaabbbb'))
print(string_composer('abcde'))
print(string_composer(''))
print(string_composer('aAbbbDDD'))
print(string_composer('aAbbbDDD', False))
print(string_composer('aaaAAAddD', False))
