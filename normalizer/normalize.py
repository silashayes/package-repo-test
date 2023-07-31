import numpy as np

def normalize(x):
    """This normalizes a bunch of numbers"""
    print("It's normalizin' time!")
    return (x - np.mean(x)) / np.std(x)