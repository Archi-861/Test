from discount_calculator import DiscountCalculator
import pytest


@pytest.fixture(scope='function')
def discount_calculator():
    return DiscountCalculator()



#положительные
@pytest.mark.dc
@pytest.mark.parametrize('price, discount, expected_price',
                         [
                             (100, 50, 50),
                             (0.1, 0.1, 0.0999)

                         ])
def test_apply_discount_positive(discount_calculator, price, discount, expected_price):

    assert discount_calculator.apply_discount(price, discount) == expected_price


#пограничные
@pytest.mark.dc
@pytest.mark.parametrize('price, discount, expected_price',
                         [
                             (100, 0, 100),
                             (100, 100, 0)

                         ])
def test_apply_discount_border(discount_calculator, price, discount, expected_price):

    assert discount_calculator.apply_discount(price, discount) == expected_price



#негативные
@pytest.mark.dc
@pytest.mark.parametrize('price, discount, expected_price',
                         [
                             (-100, 50, ValueError),
                             (100, 500, ValueError),
                             (None, 50, TypeError),

                         ])
def test_apply_discount_negative(discount_calculator, price, discount, expected_price):

    with pytest.raises(expected_price):
        discount_calculator.apply_discount(price, discount)