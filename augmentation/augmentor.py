import random

from augmentation.constants import PERIOD
from augmentation.data_helper import check_and_retrieve, _split_sentences_on_period

TEMPORARY_CONTENT = 'fake content'


def _does_not_contain_augmentation_information(example):
    return len(_split_sentences_on_period(example)) == 0


def _boolean_generator():
    return bool(random.getrandbits(1))


def _get_second_element(current_element_position, collection):
    second_number = current_element_position
    second_element_split = [TEMPORARY_CONTENT]  # TODO is this needed?

    while (second_number == current_element_position) or len(second_element_split) == 0:
        second_number = random.randint(0, len(collection) - 1)
        print(second_number)
        second_element = collection[second_number]
        second_element_split = _split_sentences_on_period(second_element)

    return collection[second_number]


def _combine_lines(first_line, second_line):
    first_line_elements = first_line.split(PERIOD)
    second_line_elements = _split_sentences_on_period(second_line)

    new_first = first_line_elements[0:len(first_line_elements) - 2]

    if len(second_line_elements) > 1:
        to_add = second_line_elements[random.randint(0, len(second_line_elements) - 2)]
    else:
        to_add = second_line_elements[0]

    new_first.append(to_add)

    return '. '.join(new_first).replace('\n', '')


def _create_new_data_line(collection, current_example, current_position, boolean_generator=_boolean_generator):
    second = _get_second_element(current_position, collection)

    if boolean_generator():
        new_line = _combine_lines(current_example, second)
    else:
        new_line = _combine_lines(second, current_example)

    return new_line


def _augment_data_for(collection):
    new_data = []

    for current_position, current_example in enumerate(collection):
        if _does_not_contain_augmentation_information(current_example):
            print('"{}" does not contain any useful augmentation information. Ignoring.'.format(current_example))
        else:
            new_data.append(_create_new_data_line(collection, current_example, current_position))

    return new_data


def _separate_into_classes(data, labels):
    results = {}

    for data_line, clazz in zip(data, labels):
        clazz_results = results.get(clazz, [])
        clazz_results.append(data_line)
        results[clazz] = clazz_results

    return results


def augment(data=None, labels=None, data_location=None, labels_location=None, rounds=1):
    # TODO checks rounds, offer possibility to only augment some classes
    retrieved_data, retrieved_labels = check_and_retrieve(data, labels, data_location, labels_location)
    for i in range(rounds):
        pass
        data_per_class = _separate_into_classes(retrieved_data, retrieved_labels)
        # then use our data per class to generate more labels

    # finally shuffle
    # and return
