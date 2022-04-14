import random
import unittest


# 1. Чтобы тестовый фреймворк понял, что это код тестов,
# а не код функций — нужно класс унаследовать от unittest.TestCase
from typing import List

from sorting import sorting


class SortingTests(unittest.TestCase):

    # 3, 2, 1
    # 1, 2, 3
    # 1  1  1
    # []
    # -10 5 -7 8
    # 3 8 5 8 2 5 9 3 8 5 8 2 5 9 3 8 5 8 2 5 9

    # Каждый отдельный метод класса — отдельный тестовый случай.
    # метод тестового случая должен начинаться с префикса test.
    def test_123(self):
        """
        Проверить, что сортируется список 3, 2, 1
        :return:
        """
        arguments: List[int] = [3, 2, 1]
        expected: List[int] = [1, 2, 3]

        # Вызываем тестируем код (подаем тестовое воздействие)
        actual_result = sorting(arguments)

        # Сравниваем с эталоном:
        self.assertEqual(expected, actual_result)

        # Так проверять результаты НЕ ПРИНЯТО!!!
        #if expected == actual_result:
        #    print('✅ Тест работает')
        #else:
        #    print('❌ Тест не работает')

    def test_ordered(self):
        """Проверить упорядоченный масссив"""
        arguments = [1, 2, 3]
        expected = [1, 2, 3]
        actual_result = sorting(arguments)
        self.assertEqual(expected, actual_result)

    def test_empty(self):
        """Проверить, что не ломается на пустом массиве []"""
        arguments = []
        expected = []
        actual_result = sorting(arguments)
        self.assertEqual(expected, actual_result)

    def test_negative(self):
        """Проверить, что сортируются отрицательные числа"""
        arguments = [-10, 5, -7, 8]
        expected = [-10, -7, 5, 8]
        actual_result = sorting(arguments)
        self.assertEqual(expected, actual_result)

    def test_float(self):
        """Сортировка вещественных чисел"""
        arguments = [5.5, 0.0, 1, .7]
        expected = [0.0, .7, 1, 5.5]
        actual_result = sorting(arguments)
        self.assertEqual(expected, actual_result)

    def test_with_standard_function(self):
        """Проверяем другим алгоритом"""
        arguments = [-10, 5, -7, 8]
        self.assertEqual(sorted(arguments), sorting(arguments))

    def test_with_random(self):
        """Проверяем случайными числами"""
        arguments = []
        for i in range (10):
            arguments.append(random.randint(0, 100))
        self.assertEqual(sorted(arguments), sorting(arguments))

    def test_min(self):
        """Проверяем, что минимлаьный элемент всегда первый"""
        arguments = []
        for i in range(10):
            arguments.append(random.randint(0, 100))
        expected_min = min(arguments)
        actual_result = sorting(arguments)
        self.assertEqual(expected_min, actual_result[0])

    def test_single_element(self):
        """Проверяем только один элемент"""
        arguments = [9]
        expected = [9]
        actual_result = sorting(arguments)
        self.assertEqual(expected, actual_result)
"""
Как проверить, что минимальная цена всегда 
находится первой на странице, всегда вначале списка.


5 10 7 8 9 15 11

5 7 8 9 10 11 15


"""