import unittest


from augmentation.data_helper import _is_not_empty_or_newline, _split_sentences_on_period, shuffle


# TODO more tests
class DataHelperTest(unittest.TestCase):
    def test_given_a_string_when_is_not_empty_or_newline_is_called_should_return_true(self):
        result = _is_not_empty_or_newline('example')

        self.assertTrue(result)

    def test_given_an_empty_string_when_is_empty_or_newline_is_called_should_return_false(self):
        result = _is_not_empty_or_newline('')

        self.assertFalse(result)

    def test_given_a_newline_when_is_not_empty_or_newline_is_called_should_return_false(self):
        result = _is_not_empty_or_newline('\n')

        self.assertFalse(result)

    def test_given_two_sentences_when_split_sentences_on_period_is_called_should_return_array_length_two(self):
        result = _split_sentences_on_period('this is the first sentence. this is the second sentence.')

        self.assertListEqual(result, ['this is the first sentence', ' this is the second sentence'])

    def tests_given_empty_string_when_split_sentences_on_period_should_return_empty_array(self):
        result = _split_sentences_on_period('')

        self.assertListEqual(result, [])
