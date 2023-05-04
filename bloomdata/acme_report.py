'''Imports'''
import random
from acme import Product

# Random lists
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    '''generate products with random attributes'''
    products = []

    for _ in range(num_products):
        name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)

        identifier = random.randint(1000000, 9999999)

        price = random.randint(5, 100)

        weight = random.randint(5, 100)

        flammability = round(random.uniform(0.0, 2.5), 2)

        products.append(Product(name, identifier, price,
                                weight, flammability))
    return products


def inventory_report(products):
    '''create an inventory report of products'''
    names = []
    total_price = 0
    total_weight = 0
    total_flammability = 0.0

    for product in products:
        names.append(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability

    avg_price = total_price / len(products)
    avg_weight = total_weight / len(products)
    avg_flammability = total_flammability / len(products)
    unique_names = set(names)
    return (len(unique_names), avg_price, avg_weight, avg_flammability)


if __name__ == '__main__':
    print(inventory_report(generate_products(30)))
