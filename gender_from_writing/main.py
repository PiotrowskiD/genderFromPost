from lxml import etree
import os
from io import StringIO
import tensorflow as tf

from word2vec import read_data, dir_path

path = "data"


def get_contents(file):
    parser = etree.HTMLParser()
    root = etree.parse(StringIO(file), parser)
    contents = root.xpath('//post/text()')

    return contents

print(read_data(dir_path))
bloggers_data = {}

for filename in os.listdir(path):
    file = open(path + "/" + filename, 'r', encoding='utf-8', errors='ignore').read()
    file = file.replace('&', '&amp;')
    file = file.replace('<Blog>', '!@#$%1')
    file = file.replace('</Blog>', '!@#$%2')
    file = file.replace('<post>', '!@#$%3')
    file = file.replace('</post>', '!@#$%4')
    file = file.replace('<date>', '!@#$%5')
    file = file.replace('</date>', '!@#$%6')
    file = file.replace('<', '&lt;')
    file = file.replace('>', '&gt;')
    file = file.replace('!@#$%1', '<Blog>')
    file = file.replace('!@#$%2', '</Blog>')
    file = file.replace('!@#$%3', '<post>')
    file = file.replace('!@#$%4', '</post>')
    file = file.replace('!@#$%5', '<date>')
    file = file.replace('!@#$%6', '</date>')
    temp_data = {
        'posts': [str(content) for content in get_contents(file)],
        'gender': filename.split(".")[1],
        'age': filename.split(".")[2]
    }
    bloggers_data[str(filename.split(".")[0])] = temp_data


log_dir = 'logs'
save_dir = 'save'
rnn_size = 256
num_layers = 2
model = 'lstm'
batch_size = 50
seq_length = 280
num_epochs = 25
save_every = 1000
grad_clip = 5.
learning_rate = 0.002
decay_rate = 0.97


