from .problem import remove_duplicates


def test_remove_duplicates():
    assert remove_duplicates([1, 1, 2]) == [2, [1, 2, "_"]]
    assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == [5, [0, 1, 2, 3, 4, "_", "_", "_", "_", "_"]]
