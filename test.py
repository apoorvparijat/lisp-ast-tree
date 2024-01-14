import unittest

from lisp_parser import LispParser


class ListParserTestCase(unittest.TestCase):
    def test_parse(self):
        parser = LispParser('(first (list 1 (+ 2 3) 9))')
        result = parser.tree_as_list()
        self.assertEqual(result, ['first', ['list', 1, ['+', 2, 3], 9]])

    def test_tokenise(self):
        parser = LispParser('(first (list 1 (+ 2 3) 9))')
        result = [token.value for token in parser.tokenise()]
        self.assertEqual(
            ['(', 'first', '(', 'list', 1, '(', '+', 2, 3, ')', 9, ')', ')'],
            result
        )