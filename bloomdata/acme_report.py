import random
from acme import Product
'''imports'''

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []

    ran_fname = random.choice(ADJECTIVES)
    ran_lname = random.choice(NOUNS)
    ran_name = ran_fname + ' ' + ran_lname

    ran_price = random.randint(5, 100)

    ran_weight = random.randint(5, 100)

    ran_flammability = random.uniform(0.0, 2.5)

    for _ in range(num_products):
        products.append(Product(
            ran_name, 0, ran_price, ran_weight, ran_flammability))

    return products


def inventory_report(products):
    unique_products = set(products)
    return len(unique_products)



if __name__ == '__main__':
 #  print(inventory_report(generate_products()))
 #  print(inventory_report(generate_products()))
    print(generate_products(4))
