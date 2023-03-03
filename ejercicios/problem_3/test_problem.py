from .problem import contain_duplicate


def test_contain_duplicate():
    assert contain_duplicate([1, 2, 3, 1]) is True
    assert contain_duplicate([1, 2, 3, 4]) is False
    assert contain_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
