from typing import List


def sorting(a: List[int]) -> List[int]:
    # Переберет индексы 0, 1, 2, 3
    for y in range(len(a)-1):
        for i in range(len(a)-1-y):
            # Это условие решает в каком порядке должны быть элементы массива
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp

    return a
