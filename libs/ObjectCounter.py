import numpy as np
import pandas as pd

class ObjectCounter():
    def __init__(self):
        pass

    # create counter dataframe
    def counter_template(self, labels, files):
        columns = ['image_name'] + labels
        counter = pd.DataFrame(np.zeros((len(files), len(columns)), dtype=int), columns=columns)

        return counter

    # add image name to table
    def add_name(self, counter, num, f):
        counter['image_name'][num] = f[:-4]

    # save info table
    def save(self, counter, directory):
        counter.to_csv(f'output/{directory}/counter.csv', index=False)