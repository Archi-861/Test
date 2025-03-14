from average import average
import pytest


#положительные
@pytest.mark.parametrize('lst, result',
                         [
                             ([1, 2, 3], 2),
                             ([1], 1),
                             ([-1], -1)

                         ])
def test_average_positive(lst, result):
    assert average(lst) == result



#негативные
@pytest.mark.parametrize('lst, result',
                         [

                             (123, TypeError),
                             ({}, ValueError),
                             ([], ValueError),
                             (0, ValueError),
                             (False, ValueError),
                             ('Rok', TypeError)

                         ])
def test_average_negative(lst, result):
    with pytest.raises(result):
        average(lst)



#пограничные
@pytest.mark.parametrize('lst, result',
                         [
                             ([0], 0),
                             ({0}, 0)



                         ])
def test_average_border(lst, result):
    assert average(lst) == result