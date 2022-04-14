from typing import List

from sorting import sorting


def test_sort_1():
    arguments: List[int] = [3, 2, 1]
    expected: List[int] = [1, 2, 3]

    actual_result = sorting(arguments)

    # Здесь пишем то условие, которое мы ожидаем.
    assert actual_result == expected
