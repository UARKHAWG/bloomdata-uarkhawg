'''Imports'''
from wallet import Wallet
import pytest

# 'decorator'
@pytest.fixture
def empty_wallet():
    '''instance of empty wallet'''
    return Wallet()

# 'decorator'
@pytest.fixture
def wallet_20():
    '''instance of wallet with balance of $20'''
    return Wallet(20)

def test_empty_wallet(empty_wallet):
    '''empty wallet test'''
    assert empty_wallet.balance == 0

def test_wallet_20(wallet_20):
    '''wallet with 20 dollars'''
    assert wallet_20.balance == 20

def test_wallet_20_spend_10(wallet_20):
    '''$20 beg balance spend 10 end with $10 balance'''
    assert wallet_20.spend_cash(10) == 'Remaining balance: $10'
    assert wallet_20.balance == 10

def test_spend_all_cash(wallet_20):
    '''spend all cash test'''
    assert wallet_20.spend_cash(20) == 'Remaining balance: $0'
