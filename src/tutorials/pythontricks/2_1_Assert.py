def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

shoes = {'name': "Fancy Shoes", 'price': 14900}
price = apply_discount(shoes, 0.25)
print("price: {}".format(price))

price = apply_discount(shoes, 2)
print("price: {}".format(price))