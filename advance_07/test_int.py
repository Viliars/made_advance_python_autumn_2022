import pytest


@pytest.mark.parametrize("value,expected", [(value, value) for value in range(-20, 20)])
def test_int_from_int(value, expected):
    result = int(value)

    assert type(result) is int
    assert int(value) == expected


@pytest.mark.parametrize(
    "value,base,expected",
    [
        ("1", 10, 1),
        ("2", 10, 2),
        ("-3", 10, -3),
        ("0", 10, 0),
        ("7", 10, 7),
        ("1000", 10, 1000),
        ("1000", 2, 8),
        ("11111", 2, 31),
        ("333", 4, 63),
        ("77", 8, 63),
    ],
)
def test_int_from_str(value, base, expected):
    result = int(value, base=base)

    assert type(result) is int
    assert int(value, base=base) == expected


@pytest.mark.parametrize(
    "value,expected", [(1.0, 1), (1.5, 1), (1.99, 1), (2.0, 2), (-3.5, -3), (0.0, 0)]
)
def test_int_from_float(value, expected):
    result = int(value)

    assert type(result) is int
    assert int(value) == expected
