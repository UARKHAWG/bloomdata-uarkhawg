'''Imports'''
from vehicle import Vehicle
import pytest

# decorator
@pytest.fixture
def dream_car():
    '''instance of dream vehicle'''
    return Vehicle('Nissan', 'GTR', 'Matte gun-metal gray', 2014, 0)

def test_make(dream_car):
    '''testing maker of car'''
    assert dream_car.make == 'Nissan'
    assert isinstance(dream_car.make, str)

def test_year(dream_car):
    '''testing year of car'''
    assert dream_car.year == 2014
    assert isinstance(dream_car.year, int)

def test_model(dream_car):
    '''testing model of car'''
    assert dream_car.model == 'GTR'
    assert isinstance(dream_car.model, str)

def test_mileage(dream_car):
    '''testing mileage'''
    assert dream_car.mileage >= 0
    assert dream_car.mileage < 100
    assert isinstance(dream_car.mileage, int)
