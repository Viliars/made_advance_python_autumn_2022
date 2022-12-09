import pytest


def test_partition_with_empty_sep():
    with pytest.raises(ValueError):
        "hello world".partition("")


def test_partition_without_args():
    with pytest.raises(TypeError):
        "hello world".partition()


@pytest.mark.parametrize(
    "string,sep,expected",
    [
        ("", "ha", ("", "", "")),
        ("h", "h", ("", "h", "")),
        ("hello world", "haha", ("hello world", "", "")),
        ("python c++ java python", "python", ("", "python", " c++ java python")),
        ("my name is", "is", ("my name ", "is", "")),
        ("i am groot", "am", ("i ", "am", " groot")),
        ("my name name", "na", ("my ", "na", "me name")),
        ("mymymy mymymy", "mymy", ("", "mymy", "my mymymy")),
        ("t1 t2 t3 t2 t2 t2", "t2", ("t1 ", "t2", " t3 t2 t2 t2")),
    ],
)
def test_partition(string: str, sep: str, expected: tuple[str, str, str]):
    result = string.partition(sep)

    assert len(result) == 3
    assert all([type(result[i]) is str for i in range(3)])
    assert string.partition(sep) == expected
