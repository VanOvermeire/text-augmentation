import unittest
from unittest.mock import patch

from augmentation.augmentor import _separate_into_classes, _get_second_element


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

        result = _get_second_element(0, data)

        self.assertEqual(result, 'example two. of three')

    @patch('random.randint')
    def test_given_data_when_get_second_element_is_called_should_return_random_element_not_equal_to_given_position(self, mocked_randint):
        data = ['example one. of three', 'example two. of three', 'example three. of three']

        mocked_randint.side_effect = [0, 1]

        result = _get_second_element(0, data)

        self.assertEqual(result, 'example two. of three')

    @patch('random.randint')
    def test_given_data_when_get_second_element_is_called_should_return_not_empty_random_element_not_equal_to_given_position(self, mocked_randint):
        data = ['example one. of three', '', 'example three. of three']

        mocked_randint.side_effect = [0, 1, 2]

        result = _get_second_element(0, data)

        self.assertEqual(result, 'example three. of three')
