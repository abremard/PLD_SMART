"""
Small script to remove empty folders in a given location
"""

import os
import sys


def remove_empty_folders(path_abs):
    if input(f"Remove empty folders in path {path_abs}? (Y/N): ").lower() != "y":
        return

    print(f"Removing empty folder in path {path_abs}")
    walk = list(os.walk(path_abs))
    for path, _, _ in walk[::-1]:
        if len(os.listdir(path)) == 0:
            os.removedirs(path)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        remove_empty_folders(sys.argv[1])
    else:
        raise Exception("Error: Please provide a path to the folder you wish to clean")
