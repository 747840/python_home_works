import pytest
from string_utils import StringUtils
string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("a", "A"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("   Skypro", "Skypro"),
    ("   Hello world", "Hello world"),
    ("   Skypro   ", "Skypro   "),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("string, symbol, result", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("123", "2", True),
])
def test_contains_positive(string, symbol, result):
    assert string_utils.contains(string, symbol) == result


@pytest.mark.parametrize("string, symbol, new_string", [
    ("SkyPro", "S", "kyPro"),
    ("Sky Pro", " ", "SkyPro"),
    ("14899", "99", "148"),
])
def test_delete_symbol_positive(string, symbol, new_string):
    assert string_utils.delete_symbol(string, symbol) == new_string


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("Skypro   ", "Skypro   "),
    ("Hello   world", "Hello   world"),
    ("Skypro", "Skypro"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("string, symbol, result", [
    ("SkyPro", "", True),
    ("", "U", False),
    ("   ", "2", False),
])
def test_contains_negative(string, symbol, result):
    assert string_utils.contains(string, symbol) == result


@pytest.mark.parametrize("string, symbol, new_string", [
    ("", "A", ""),
    ("SkyPro", "U", "SkyPro"),
    ("14899", "", "14899"),
    ("banana", "a", "bnn"),
])
def test_delete_symbol_negative(string, symbol, new_string):
    assert string_utils.delete_symbol(string, symbol) == new_string
