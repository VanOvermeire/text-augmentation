import random
from typing import List

from augmentation.constants import PERIOD
from augmentation.data_helper import check_and_retrieve, _split_sentences_on_period, shuffle


def _contains_augmentation_information(example):
    return len(_split_sentences_on_period(example)) > 0


def _get_a_second_element(current_element_position, collection):
    second_element = ''
    second_position = current_element_position
    second_element_split = []

    while (second_position == current_element_position) or len(second_element_split) == 0:
        second_position = random.randint(0, len(collection) - 1)
        second_element = collection[second_position]
        second_element_split = _split_sentences_on_period(second_element)

    return second_element


def _combine_lines(first_line, second_line):
    """
        Combines two lines by taking the first line without the last sentence, together
        with a sentence from the second line
    """
    first_line_elements = _split_sentences_on_period(first_line)
    second_line_elements = _split_sentences_on_period(second_line)

    new_first = first_line_elements[0:len(first_line_elements) - 1]
    to_add = second_line_elements[random.randint(0, len(second_line_elements) - 1)]
    new_first.append(to_add)

    return PERIOD.join(new_first)


def _create_new_data_line(collection, current_example, current_position):
    second = _get_a_second_element(current_position, collection)

    if bool(random.getrandbits(1)):
        new_line = _combine_lines(current_example, second)
    else:
        new_line = _combine_lines(second, current_example)

    return new_line


def _augment_data_for(collection):
    new_data = []

    for current_position, current_example in enumerate(collection):
        if _contains_augmentation_information(current_example):
            new_data.append(_create_new_data_line(collection, current_example, current_position))
        else:
            print('"{}" does not contain any useful augmentation information. Ignoring.'.format(current_example))

    return new_data


def _separate_into_classes(data, labels):
    results = {}

    for data_line, clazz in zip(data, labels):
        clazz_results = results.get(clazz, [])
        clazz_results.append(data_line)
        results[clazz] = clazz_results

    return results


def augment(data: List[str] = None, labels: List[str] = None, data_location: str = None, labels_location: str = None, rounds: int = 1):
    # TODO checks rounds, offer possibility to only augment some classes
    retrieved_data, retrieved_labels = check_and_retrieve(data, labels, data_location, labels_location)
    unshuffled_data = []
    unshuffled_labels = []

    for i in range(rounds):
        data_per_class = _separate_into_classes(retrieved_data, retrieved_labels)

        for k, v in data_per_class.items():
            unshuffled_data.extend(v)
            unshuffled_labels.extend([k for x in v])

            augmented = _augment_data_for(v)
            unshuffled_data.extend(augmented)
            unshuffled_labels.extend([k for x in augmented])

    return shuffle(unshuffled_data, unshuffled_labels)
