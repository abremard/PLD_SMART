"""
Scripts for editing the Firebase database
"""
import os
import sys
from database.metadata_processing import *
from database.firestore import *


def get_formatted_file_path(file_path: str) -> str:
    """
    Only format the file name, then return the whole path with the new file name
    Args:
        file_path: The path to format

    Returns: The formatted file path

    """

    split_path = file_path.split("/")
    path_to_file = "" if len(split_path) == 1 else "/".join(split_path[:-1])
    file_name = split_path[-1].split(".")[0]
    formatted_name = format_string(file_name)
    return f"{path_to_file}/{formatted_name}.{file_path.split('.')[-1]}"


def rename_files_in_dir(directory_path: str):
    directory = os.path.dirname(directory_path)
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            subdir_path = os.path.relpath(subdir, directory)  # get the path to the subdirectory
            file_path = os.path.join(subdir_path, filename)  # get the path to the file
            new_file_path = get_formatted_file_path(file_path)
            os.rename(file_path, new_file_path)  # rename your file


def upload_files_from_dir(directory_path: str):
    rename_files_in_dir(directory_path)


def main():
    upload_files_from_dir(sys.argv[1])
    pass


if __name__ == '__main__':
    # main()
    get_formatted_file_path("abc.mid")
