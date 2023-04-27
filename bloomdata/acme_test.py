'''Imports'''
from acme import Product
import pytest

# decorator
@pytest.fixture
def test_prod():
    return Product('Iphone', 9814891, 1000, 2.875, .29)

# decorator
@pytest.fixture
def default_prod_values():
    return Product(name='', identifier='', price=10, weight=20, flammability=0.5)

def test_default_prod_values(default_prod_values):
    '''default values test'''
    assert default_prod_values.price == 10
    assert default_prod_values.weight == 20
    assert default_prod_values.flammability == 0.5

def name_type_test(test_prod):
    '''type test'''
    assert isinstance(test_prod.name, int)
    