import random
import pandas as pd

def btstrap(InitialSample, seed):
    sample = InitialSample.sample(n = 9, random_state = seed, replace = True)
    OutOfBageSample = sample.drop_duplicates()
    OutOfBageSample = InitialSample.drop(labels=OutOfBageSample.index)
    return sample, OutOfBageSample

