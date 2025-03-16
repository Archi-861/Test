from data_processor import DataProcessor
import pytest, json, os


@pytest.fixture(scope='module')
def json_file():

    path_to_json_file = 'json_file.json'

    data = {
        'student': 'Harry Potter',
        'faculty': 'Griffindor',
        'spell': 'Patronym'
    }

    with open (path_to_json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file)

    data_processor = DataProcessor(file_path=path_to_json_file)

    yield data_processor

    os.remove(path_to_json_file)


#положительные
@pytest.mark.dp
@pytest.mark.parametrize('key, expected_result',
                         [
                             ('student', 'Harry Potter'),
                             ('faculty', 'Griffindor'),
                             ('spell', 'Patronym')
                         ])
def test_load_data_positive(json_file, key, expected_result):

    assert json_file.get_value(key) == expected_result



#пограничные
@pytest.mark.dp
@pytest.mark.parametrize('key, expected_result',
                         [
                             (None, None),
                             ('', None),
                             (1, None),
                             (1.5, None),
                             ('abc', None),
                             ('student_1', None)

                         ])
def test_load_data_border(json_file, key, expected_result):

    assert json_file.get_value(key) == expected_result



#негативные
@pytest.mark.dp
@pytest.mark.parametrize('key, expected_result',
                         [
                             ({}, TypeError),
                             ([], TypeError)

                         ])
def test_load_data_negative(json_file, key, expected_result):

    with pytest.raises(expected_result):

        json_file.get_value(key)


