'''imports'''
import helper_functions as hf

adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']

nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

list1 = [1, 2, 3]
list2 = [4, 5, 6]

def test_random_phrase():
    '''random phrase test'''
    #assert type(hf.random_phrase()) == str
    assert isinstance(hf.random_phrase(), str)

def test_random_phrase2():
    '''random phrase test of lists'''    
    #assert type(hf.random_phrase2(list1, list2)) == str
    assert isinstance(hf.random_phrase2(list1, list2), str)
    #assert isinstance(hf.random_phrase2(list1, list2), int)
    assert hf.random_phrase2(['James'], ['Bond']) == 'James Bond'
    assert hf.random_phrase2(['3'], ['4']) == '3 4'
