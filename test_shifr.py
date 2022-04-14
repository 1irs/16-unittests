import unittest

from shifr import shifr


# class SignUpTests
# class SearchTests
# class AllTests
class ShifrTests(unittest.TestCase):

    def test_hello(self):
        """Протестировать на слове ПРИВЕТ"""
        argument = "ПРИВЕТ"
        expected = "ПРИсИВЕсЕТ"

        actual_result = shifr(argument)
        self.assertEqual(expected, actual_result)

    def test_empty(self):
        """UC3 Encrypt meesage. FR1 Empty messages must be processed"""
        argument = ""
        expected = ""

        actual_result = shifr(argument)
        self.assertEqual(expected, actual_result)

    def test_none(self):
        """UC3 Encrypt meesage. FR1 Empty messages must be processed"""
        argument = None
        expected = ""

        actual_result = shifr(argument)
        self.assertEqual(expected, actual_result)

    def test_no_changes(self):
        """Без изменений"""
        self.assertEqual("КЛМНПРСТ", shifr("КЛМНПРСТ"))
