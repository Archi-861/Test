from bank_account import BankAccount
import pytest



#положительные
@pytest.mark.parametrize('initial_balance, withdraw_amount, result',
                         [
                             (100, 50, 50),
                             (100, 100, 0)


                         ])
def test_withdraw_positive(initial_balance, withdraw_amount, result):
    account = BankAccount()
    account.deposit(initial_balance)
    account.withdraw(withdraw_amount)
    assert account.get_balance() == result



#негативные
@pytest.mark.parametrize('withdraw_amount, result',
                         [
                             (1000, ValueError),
                             (-10, ValueError),
                             (None, TypeError),




                         ])
def test_withdraw_negative(withdraw_amount, result):
    with pytest.raises(result):
        account = BankAccount()
        account.deposit(100)
        account.withdraw(withdraw_amount)
        account.get_balance()


#пограничные
@pytest.mark.parametrize('initial_balance, withdraw_amount, result',
                         [

                             (100, 100, 0),



                         ])
def test_withdraw_border(initial_balance, withdraw_amount, result):
    account = BankAccount()
    account.deposit(initial_balance)
    account.withdraw(withdraw_amount)
    assert account.get_balance() == result