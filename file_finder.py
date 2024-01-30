import os

"""
@author: Andrew Anca
"""

"""This module houses the file finder function"""


class FileFinder:
    def __init__(self):
        pass

    def get_current_directory(self):
        print(os.getcwd())
        return os.getcwd()

    def get_parent_directory(self, directory):
        print(os.path.dirname(directory))
        return os.path.dirname(directory)

    def print_files(self, directory):
        for file in os.listdir(directory):
            if file.endswith('.py'):
                print(file)
