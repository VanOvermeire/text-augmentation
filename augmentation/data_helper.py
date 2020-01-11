import re

from augmentation.checks import check_data_and_labels
from augmentation.constants import PERIOD
from augmentation.data_reader import get_data


def _is_not_empty_or_newline(example):
    return example != '' and example != '\n'


def _split_sentences_on_period(example):
    return [x for x in example.split(PERIOD) if _is_not_empty_or_newline(x)]


def _clean(data):
    """ Cleans our data
        We can't handle ';' since we use that to separate data from labels
        Also remove linebreaks, tabs and multiple spaces which might cause issues too
    """
    first_clean = [d.replace(';', ' ').replace('\n', '').replace('\t', '').strip() for d in data]
    return [re.sub(' {2,}', ' ', elem) for elem in first_clean]


def check_and_retrieve(data=None, labels=None, data_location=None, labels_location=None):
    check_data_and_labels(data, labels, data_location, labels_location)

    if data_location is not None:
        retrieved_data, retrieved_labels = get_data(data_location, labels_location)
        return _clean(retrieved_data), _clean(retrieved_labels)
    return _clean(data), _clean(labels)
