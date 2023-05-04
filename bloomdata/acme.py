'''Imports'''
import random


class Product:
    '''Create Product class'''
    def __init__(self,
                 name,
                 identifier=random.randint(1000000, 9999999),
                 price=10,
                 weight=20,
                 flammability=0.5) -> None:
        self.name = name
        self.identifier = identifier
        self.price = price
        self.weight = weight
        self.flammability = flammability

    def stealability(self):
        '''func method docstring'''
        if (self.price / self.weight) < 0.5:
            return 'Not so stealable'
        if ((self.price / self.weight) >= 0.5) \
                & ((self.price / self.weight) < 1):
            return 'Kinda stealable'
        return 'Very stealable!'

    def explode(self):
        '''func method docstring'''
        if (self.flammability * self.weight) < 10:
            return 'fizzle'
        if ((self.flammability * self.weight) >= 10) \
                & ((self.flammability * self.weight) < 50):
            return 'boom!'
        return 'BABOOM!!'


class BoxingGlove(Product):
    '''create child class'''
    def __init__(self,
                 name,
                 identifier=random.randint(1000000, 9999999),
                 price=10,
                 weight=10,
                 flammability=0.5) -> None:
        super().__init__(name,
                         identifier,
                         price,
                         weight,
                         flammability)

    def explode(self):
        '''fun medthod docstring'''
        return "...it's a glove."

    def punch(self):
        '''func method docstring'''
        if self.weight < 5:
            return 'That tickles.'
        elif 5 <= self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
