import unittest

from augmentation.data_helper import _clean


# TODO more tests, check naming
class CheckTest(unittest.TestCase):
    def test_clean(self):
        filthy_data = ['this has  spaces', 'this \n a newline', 'a \t', 'a ; which we do not want', 'and \n this has; multiple  issues ']

        results = _clean(filthy_data)

        self.assertEqual(results[0], 'this has spaces')
        self.assertEqual(results[1], 'this a newline')
        self.assertEqual(results[2], 'a')
        self.assertEqual(results[3], 'a which we do not want')
        self.assertEqual(results[4], 'and this has multiple issues')
