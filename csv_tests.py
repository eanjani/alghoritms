import pytest

WORDSLIST = 'C:/Users/Anna/Desktop/english-words.csv'

@pytest.fixture()
def csv_data():
    with open(WORDSLIST, 'r') as f:
        lines = f.readlines()
    data = [line.strip() for line in lines]
    return data

@pytest.fixture()
def csv_header(csv_data):
    return csv_data[0]

@pytest.fixture()
def csv_records(csv_data):
    return csv_data[1:]

@pytest.fixture()
def column_names(csv_header):
    return csv_header.split(";")


def test_header_starts_with_id(column_names):
    """ Check if first field in header is ID """
    first_col_name = column_names[0]
    assert first_col_name == 'id'

def test_header_has_col_word(column_names):
    assert 'word' in column_names


def test_header_has_col_frequence(column_names):
    assert 'frequence' in column_names

    
def test_records_matches_header(column_names,csv_records):
    """ Check if amount of data in record is the same like in header """
    header_col_count = len(column_names)
    errors = []

    for record in csv_records:
        record_values = record.split(';')
        record_values_count = len(record_values)
        if record_values_count != header_col_count:
            errors.append(record)
        assert not errors


def test_first_field_numerical(csv_records):
    """ check that 1st and 3rd field of each record is numerical """
    errors = []

    for record in csv_records:
        record_values = record.split(";")
        if not record_values[0].isdigit():
            errors.append(record)
    assert not errors

def test_second_field_word(csv_records):
    """ check if 2nd value is a word """
    errors = []

    for record in csv_records:
        record_values = record.split(";")
        if record_values[1].isdigit():
            errors.append(record)
        assert not errors
