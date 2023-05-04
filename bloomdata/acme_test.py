'''Imports'''
import pytest
from acme import Product
from acme_report import generate_products, inventory_report


@pytest.fixture
def default_prod_values():
    ''' decorator'''
    return Product('Product Template')


@pytest.fixture
def test_prod():
    ''' decorator'''
    return Product('Iphone', 9814891, 1000, 2.875, 0.95)


@pytest.fixture
def test_prod2():
    ''' decorator'''
    return Product('Starlink Kit', 9814893, 10, 7800, 10.8)


@pytest.fixture
def prod_list():
    ''' decorator'''
    return generate_products()


@pytest.fixture
def report_list():
    '''decorator'''
    return inventory_report(generate_products())


def test_explode(default_prod_values, test_prod, test_prod2):
    '''test explode method of Product class'''
    assert default_prod_values.explode() == 'boom!'
    assert test_prod.explode() == 'fizzle'
    assert test_prod2.explode() == 'BABOOM!!'


def test_stealability(default_prod_values, test_prod, test_prod2):
    '''test stealability method of Product class'''
    assert default_prod_values.stealability() == 'Kinda stealable'
    assert test_prod.stealability() == 'Very stealable!'
    assert test_prod2.stealability() == 'Not so stealable'


def test_data_type(default_prod_values):
    '''type test'''
    assert isinstance(default_prod_values.name, str)
    assert isinstance(default_prod_values.identifier, int)
    assert isinstance(default_prod_values.price, int)
    assert isinstance(default_prod_values.weight, int)
    assert isinstance(default_prod_values.flammability, float)


def test_default_prod_values(default_prod_values):
    '''default values test'''
    assert default_prod_values.price == 10
    assert default_prod_values.weight == 20
    assert default_prod_values.flammability == 0.5


def test_default_num_prod(prod_list):
    '''test default product list count'''
    assert len(prod_list) == 30
