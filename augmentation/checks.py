# TODO tests
def check_data_and_labels(data=None, labels=None, data_location=None, labels_location=None):
    if data_location is None and labels_location is None and data is None and labels is None:
        raise ValueError('Need locations OR arrays')
    if (data_location is not None and labels_location is None) or (data_location is None and labels_location is not None):
        raise ValueError('Need both data AND label location')
    if (data is not None and labels is None) or (data is None and labels is not None):
        raise ValueError('Need both data AND labels')
    if data is not None and type(data) is not list:
        raise ValueError('Data is {} instead of list'.format(type(data)))
    if labels is not None and type(labels) is not list:
        raise ValueError('Labels is {} instead of list'.format(type(labels)))
    if (data is not None and labels is not None) and len(data) != len(labels):
        raise ValueError('Data was length {} while labels was {}'.format(len(data), len(labels)))
    if data_location is not None and type(data_location) is not str:
        raise ValueError('Expected data_location to be a string but was {}'.format(type(data_location)))
    if labels_location is not None and type(labels_location) is not str:
        raise ValueError('Expected labels_location to be a string but was {}'.format(type(labels_location)))
