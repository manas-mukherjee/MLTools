
def process_using_div(list_input):
    list_output = []

    prod = 1
    for i in list_input:
        prod *= i

    for i in list_input:
        list_output.append(int(prod/i))

    print(list_output)


def process_without_using_div(list_input):
    print(list_input)
    pref_products = []

    for num in list_input:
        if pref_products:
            pref_products.append(num * pref_products[-1])
        else:
            pref_products.append(num)

    print(pref_products)

    post_products = []

    for num in reversed(list_input):
        if post_products:
            post_products.append(num * post_products[-1])
        else:
            post_products.append(num)

    print(list(reversed(post_products)))


if __name__ == "__main__":
    l = [1,2,3,4,5]
    # l = [3,2,1]
    process_using_div(l)
    process_without_using_div(l)