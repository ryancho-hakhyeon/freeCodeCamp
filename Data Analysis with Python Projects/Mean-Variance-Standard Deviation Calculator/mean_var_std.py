import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    else:
        temp = np.array(list).reshape(3, 3)

    calculations = {
        'mean': [temp.mean(axis=0).tolist(), temp.mean(axis=1).tolist(), temp.mean()],
        'variance': [temp.var(axis=0).tolist(), temp.var(axis=1).tolist(), temp.var()],
        'standard deviation': [temp.std(axis=0).tolist(), temp.std(axis=1).tolist(), temp.std()],
        'max': [temp.max(axis=0).tolist(), temp.max(axis=1).tolist(), temp.max()],
        'min': [temp.min(axis=0).tolist(), temp.min(axis=1).tolist(), temp.min()],
        'sum': [temp.sum(axis=0).tolist(), temp.sum(axis=1).tolist(), temp.sum()]
    }
    return calculations