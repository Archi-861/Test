from bank_account import BankAccount
import pytest


@pytest.fixture(scope='function')
def bank_account():
    return BankAccount(100)



#положительные
@pytest.mark.ba_withdraw
@pytest.mark.parametrize('amount, result',
                         [
                             (50, 50),
                             (0.01, 99.99)


                         ])
def test_withdraw_positive(bank_account, amount, result):
    assert bank_account.withdraw(amount) == result



#пограничные
@pytest.mark.ba_withdraw
@pytest.mark.parametrize('amount, result',
                         [
                             (100, 0),
                             (0, 100),
                             (-10, 110)



                         ])
def test_withdraw_border(bank_account, amount, result):
    assert bank_account.withdraw(amount) == result



#негативные
@pytest.mark.ba_withdraw
@pytest.mark.parametrize('amount, result',
                         [
                             ('abc', TypeError),
                             ([], TypeError),
                             (None, TypeError),


                         ])
def test_withdraw_negative(bank_account, amount, result):
    with pytest.raises(result):
        bank_account.withdraw(amount)



