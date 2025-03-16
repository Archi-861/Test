from logger import Logger
import pytest
import os



@pytest.fixture(scope='function')
def logger():
    path_to_test_file = 'test_log.txt'
    logger = Logger(file_path=path_to_test_file)

    yield logger

    os.remove(path_to_test_file)


#положительные
@pytest.mark.log
@pytest.mark.parametrize('message, expected_result',
                         [
                             ('abc', 'abc'),
                             ('123', '123')
                         ])
def test_logger_log_positive(logger, message, expected_result):
    logger.log(message)

    assert logger.get_logs()[0].replace('\n', '') == expected_result



#пограничные
@pytest.mark.log
@pytest.mark.parametrize('message, expected_result',
                         [
                             ('', ''),
                             ('"100"', '"100"')

                         ])
def test_logger_log_border(logger, message, expected_result):
    logger.log(message)

    assert logger.get_logs()[0].replace('\n', '') == expected_result



#негативные
@pytest.mark.log
@pytest.mark.parametrize('message, expected_result',
                         [
                             (-1, TypeError),
                             (None, TypeError),
                             ([123], TypeError),
                             ({}, TypeError)

                         ])
def test_logger_log_negative(logger, message, expected_result):

    with pytest.raises(expected_result):
        logger.log(message)

        logger.get_logs()[0].replace('\n', '')
