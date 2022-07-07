"""Ensure that the data transformation works correctly."""

from dataanalysis import transform


def test_transform_empty_text_list_to_number_list():
    """Ensure that an empty list of textual numbers transforms correctly."""
    data_list_string = ""
    data_list_numbers = transform.transform_string_to_number_list(data_list_string)
    assert len(data_list_numbers) == 0
    assert sum(data_list_numbers) == 0
    assert data_list_numbers == []


def test_transform_small_text_list_to_number_list():
    """Ensure that a small list of textual numbers transforms correctly."""
    data_list_string = """1970-01-0,10
1970-01-0,5
1970-01-0,10
1970-01-0,5
1970-01-0,10"""
    data_list_numbers = transform.transform_string_to_number_list(data_list_string)
    assert len(data_list_numbers) == 5
    assert sum(data_list_numbers) == 10 + 5 + 10 + 5 + 10
    assert data_list_numbers == [10, 5, 10, 5, 10]
