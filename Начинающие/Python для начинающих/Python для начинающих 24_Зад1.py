import unittest
from unittest.mock import patch

class Dictionary:
    def __init__(self):
        self.terms = {}

    def add_term(self, term, definition):
        if term in self.terms:
            return "Термин уже существует в словаре."
        else:
            self.terms[term] = definition
            return "Термин добавлен в словарь."

    def look_up(self, term):
        if term in self.terms:
            return self.terms[term]
        else:
            return "Термин не найден в словаре."

    def remove_term(self, term):
        if term in self.terms:
            del self.terms[term]
            return "Термин удален из словаря."
        else:
            return "Термин не найден в словаре."


class TestDictionary(unittest.TestCase):

    def test_add_term(self):
        dictionary = Dictionary()
        result1 = dictionary.add_term("Python", "Язык программирования")
        self.assertEqual(result1, "Термин добавлен в словарь.")
        result2 = dictionary.add_term("Python", "Другое определение")
        self.assertEqual(result2, "Термин существует в словаре.")

    def test_look_up(self):
        dictionary = Dictionary()
        dictionary.add_term("Python", "Язык программирования")
        self.assertEqual(dictionary.look_up("Python"), "Язык программирования")
        self.assertEqual(dictionary.look_up("Java"), "Термин не найден в словаре.")

    def test_remove_term(self):
        dictionary = Dictionary()
        dictionary.add_term("Python", "Язык программирования")
        result1 = dictionary.remove_term("Python")
        self.assertEqual(result1, "Термин удален из словаря.")
        result2 = dictionary.remove_term("Java")
        self.assertEqual(result2, "Термин не найден в словар.")

if __name__ == '__main__':
    unittest.main()
