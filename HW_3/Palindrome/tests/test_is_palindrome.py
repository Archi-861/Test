from palindrome import is_palindrome
import pytest


#положительные
@pytest.mark.parametrize('s, result',
                         [
                             ('поп', True),
                             ('Поп', False),
                             ('Рок', False),
                             ('123321', True)


                         ])
def test_is_palindrome_positive(s, result):
    assert is_palindrome(s) == result



#негативные
@pytest.mark.parametrize('s, result',
                         [

                             (123, TypeError),
                             ([123], TypeError),
                             (None, TypeError),
                             ({131}, TypeError),
                             ([], TypeError)


                         ])
def test_is_palindrome_negative(s, result):
    with pytest.raises(result):
        is_palindrome(s)



#пограничные
@pytest.mark.parametrize('s, result',
                         [
                             ('', True)


                         ])
def test_is_palindrome_border(s, result):
    assert is_palindrome(s) == result