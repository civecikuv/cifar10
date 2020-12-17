from PIL import Image
import numpy as np
import os
PATH = os.path.dirname(__file__)


def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def show_data(dict,num_imgs):
    data = dict[b'data'].reshape(-1, 32, 32, 3)
    for i in range(0,num_imgs):
        img = Image.fromarray(data[i], 'RGB')
        img.show()

batch1="cifar-10-batches-py/data_batch_1"
dict = unpickle(os.path.join(PATH,batch1))
show_data(dict,5)

data = dict[b'data'].reshape(-1,3,32,32)
labels = dict[b'labels']

