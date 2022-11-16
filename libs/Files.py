import os
import re

class Files():
    def __init__(self):
        pass

    # list of image names
    def image_list(self, path):
        # files list
        p = re.compile('.*\.jpeg|.*\.jpg|.*\.png')
        files_all = os.listdir(path)
        # leave only images
        files = [s for s in files_all if p.match(s)]

        return files

    # create a directory where to save the results
    def create_res_dir(self, directory):
        os.mkdir(f'output/{directory}')