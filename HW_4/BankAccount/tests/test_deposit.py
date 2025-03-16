from bank_account import BankAccount
import pytest



@pytest.fixture(scope='module')
def bank_account():
    return {
        'ba': BankAccount()
    }

#положительные
@pytest.mark.ba_deposit
@pytest.mark.parametrize('amount, result',
                         [
                             (100, 100),
                             (0.1, 0.1),

                         ])
def test_deposit_positive(bank_account, amount, result):
    bank_account['ba'].balance = 0
    assert bank_account['ba'].deposit(amount) == result


#пограничные
@pytest.mark.ba_deposit
@pytest.mark.parametrize('amount, result',
                         [
                             (0, 0),
                             (0.0000000000000000000000000000001, 0.0000000000000000000000000000001)
                         ])
def test_deposit_border(bank_account, amount, result):
    bank_account['ba'].balance = 0
    assert bank_account['ba'].deposit(amount) == result



#негативные
@pytest.mark.ba_deposit
@pytest.mark.parametrize('amount, result',
                         [
                             (-1, ValueError),
                             ('abc', TypeError),
                             ([], TypeError),
                             (None, TypeError),


                         ])
def test_deposit_negative(bank_account, amount, result):
    bank_account['ba'].balance = 0
    with pytest.raises(result):
        bank_account['ba'].deposit(amount)
