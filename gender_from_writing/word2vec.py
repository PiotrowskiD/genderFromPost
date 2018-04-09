import os
import tensorflow as tf

dir_path = "data"


def read_data(path):
    """Extract all files in dir as a list of words."""
    data = ''

    for f in os.listdir(path):
        data = data + tf.compat.as_str(str(open(path + '/' + f, 'r', encoding='utf-8', errors='ignore').read().split()))
        print(data)
        print('/n')
    return data


def build_dataset(words, n_words):
    """Process raw inputs into a dataset."""
    count = [['UNK', -1]]
    count.extend(tf.collections.Counter(words).most_common(n_words - 1))
    dictionary = dict()
    for word, _ in count:
        dictionary[word] = len(dictionary)
    data = list()
    unk_count = 0
    for word in words:
        if word in dictionary:
            index = dictionary[word]
        else:
            index = 0  # dictionary['UNK']
            unk_count += 1
        data.append(index)
    count[0][1] = unk_count
    reversed_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    return data, count, dictionary, reversed_dictionary
