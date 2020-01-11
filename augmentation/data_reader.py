def get_data(data_location, labels_location):
    # how big a dataset can method for retrieving files handle?
    with open(data_location, 'r') as data_set, open(labels_location, 'r') as labels:
        data = data_set.readlines()
        labels = labels.readlines()

        return data, labels
