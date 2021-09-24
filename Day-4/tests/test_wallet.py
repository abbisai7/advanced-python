import pytest

from wallet import Wallet,InsufficientFunds

def test_default():
    wallet = Wallet()
    wallet.balance = 100
    assert wallet.balance == 100
    
def test_add_cash():
    wallet = Wallet(200)
    wallet.add_cash(100)
    assert wallet.balance == 300
    
def test_spend_cash():
    wallet = Wallet(300)
    wallet.spend_cash(100)
    assert wallet.balance == 200
    
def test_for_exceptions():
    wallet = Wallet(100)
    with pytest.raises(InsufficientFunds):
        wallet.spend_cash(200)
        #assert wallet.balance == 200