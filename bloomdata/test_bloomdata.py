'''imports'''
import bloomdata


def test_increment_int():
    '''increment func test'''
    assert bloomdata.increment(3) == 4
    assert bloomdata.increment(-1) == 0

def test_increment_float():
    '''increment func float test'''
    assert bloomdata.increment(1.5) == 2.5

def test_increment_int_return_type():
    '''increment func type test'''
    assert isinstance(bloomdata.increment(3), int)
