import numpy as np

def make_data():
    data = np.random.random(size=10)
    np.save('./data/test_data.npy', data)
    return