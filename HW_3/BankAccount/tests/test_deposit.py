from bank_account import BankAccount
import pytest


#положительные
@pytest.mark.parametrize('amount, result',
                         [
                             (100, None),
                             (0.1, None),
                             (0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000001, None)

                         ])
def test_deposit_positive(amount, result):
    assert BankAccount().deposit(amount) == result



#негативные
@pytest.mark.parametrize('amount, result',
                         [

                             (-1, ValueError),
                             (0, ValueError),
                             ({}, TypeError),
                             (False, ValueError),
                             ([1], TypeError),
                             ('1', TypeError),
                             (None, TypeError)

                         ])
def test_deposit_negative(amount, result):
    with pytest.raises(result):
        BankAccount().deposit(amount)



#пограничные
@pytest.mark.parametrize('amount, result',
                         [
                             (True, None),


                         ])
def test_deposit_border(amount, result):
    assert BankAccount().deposit(amount) == result