import unittest
from unittest.mock import patch

from augmentation.augmentor import _separate_into_classes, _get_a_second_element, _combine_lines, _create_new_data_line, _augment_data_for


class AugmentationTest(unittest.TestCase):
    def test_given_data_and_labels_when_separate_into_classes_is_called_should_create_dict_classes_as_keys(self):
        data = ['example. of the second class', 'an example of. the first class', 'and an example of the second class.']
        labels = [1, 0, 3]

        results = _separate_into_classes(data, labels)

        self.assertEqual(results, {1: ['example. of the second class'], 0: ['an example of. the first class'], 3: ['and an example of the second class.']})

    @patch('random.randint')
    def test_given_data_when_get_second_element_is_called_should_return_random_element(self, mocked_randint):
        data = ['example one. of three', 'example two. of three', 'example three. of three']

        mocked_randint.return_value = 1

        result = _get_a_second_element(0, data)

        self.assertEqual(result, 'example two. of three')

    @patch('random.randint')
    def test_given_data_when_get_second_element_is_called_should_return_random_element_not_equal_to_given_position(self, mocked_randint):
        data = ['example one. of three', 'example two. of three', 'example three. of three']

        mocked_randint.side_effect = [0, 1]

        result = _get_a_second_element(0, data)

        self.assertEqual(result, 'example two. of three')

    @patch('random.randint')
    def test_given_data_when_get_second_element_is_called_should_return_not_empty_random_element_not_equal_to_given_position(self, mocked_randint):
        data = ['example one. of three', '', 'example three. of three']

        mocked_randint.side_effect = [0, 1, 2]

        result = _get_a_second_element(0, data)

        self.assertEqual(result, 'example three. of three')

    @patch('random.randint')
    def test_given_two_lines_when_combine_lines_combines_them_into_a_new_example(self, mocked_randint):
        first_line = 'this is the first. example which has. three sentences'
        second_line = 'followed by the second example. two instead.'

        mocked_randint.return_value = 1

        result = _combine_lines(first_line, second_line)

        self.assertEqual(result, 'this is the first. example which has. two instead')

    @patch('random.getrandbits')
    @patch('random.randint')
    def test_given_collection_element_and_position_when_create_new_data_line_is_called_should_return_new_example(self, mocked_randint, mocked_getrandbits):
        collection = ['this is the first. example which has. three sentences', 'followed by the second example. two instead.', 'with a third one. at the end of the array']

        mocked_randint.return_value = 1
        mocked_getrandbits.return_value = 1

        result = _create_new_data_line(collection, 'this is the first. example which has. three sentences', 0)

        self.assertEqual(result, 'this is the first. example which has. two instead')

    @patch('random.getrandbits')
    def test_given_collection(self, mocked_getrandbits):
        collection = ['this is the first. example which has. three sentences', 'followed by the second example. two instead.', 'with a third one. at the end of the array']

        mocked_getrandbits.return_value = 1

        result = _augment_data_for(collection)

        self.assertTrue(result[0], 'this is the first. example which has.')
        self.assertTrue(result[1], 'followed by the second example.')
        self.assertTrue(result[2], 'with a third one.')
