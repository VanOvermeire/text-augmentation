# Text Augmentation

Uses your existing text data to generate additional (augmented) examples, improving validation accuracy on (small) datasets.

Demonstration code for [this][1] blog post.

[1]: https://www.linkedin.com/pulse/augmenting-text-data-sam-van-overmeire/

## Usage

`x, y = augment(data_location='./data', labels_location='../labels')`

The augment function expects text files, with one instance/label per line. You can
pass the location of the file (as in the above example), or the files itself:

`x, y = augment(data=data_loaded_into_python, labels=labels_loaded_into_python)`
