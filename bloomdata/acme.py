'''Imports'''
#import pytest
import random

#class Product:

class Product:
    '''Create Product class'''
    price = 10
    weight = 20
    flammability = 0.5
    def __init__(self, name, identifier, price, weight, flammability):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)



    def stealability(self):
        '''func method docstring'''
        if (self.price / self.weight) < 0.5:
            return 'Not so stealable'
        elif ((self.price / self.weight) >= 0.5) & ((self.price / self.weight) < 1):
            return 'Kinda stealable'
        else:
            return 'Very stealable!'

    def explode(self):
        '''func method docstring'''
        if (self.flammability * self.weight) < 10:
            return 'fizzle'
        if ((self.flammability * self.weight) >= 10) & ((self.flammability * self.weight) < 50):
            return 'boom!'
        return 'BABOOM!!'

if __name__ == '__main__':
    prod = Product('soap', 0, 100, 27.2, 2.3)

    print(f'Product name: {prod.name}')
    print(f'Product identifier: {prod.identifier}')
    print(f'Product price: {prod.price}')
    print(f'Product weight: {prod.weight}')
    print(f'Flammability: {prod.flammability}')

    print(prod.stealability())

class BoxingGlove(Product):
    '''create child class'''
    def __init__(self, name, identifier, price, weight, flammability):
        super().__init__(name, identifier, price, weight, flammability)
    weight = 10

    def explode(self):
        '''fun medthod docstring'''
        return "...it's a glove."

    def punch(self):
        '''func method docstring'''
        weight = 10
        if weight < 5:
            return 'That tickles'
        if weight >= 5 and weight > 15:
            return 'Hey that hurt!'
        return 'OUCH!'
        