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

    # rename files to a correct format
    print(f"Renaming files in {directory_path}")
    # rename_files_in_dir(directory_path)       # todo uncomment when ok

    # file by file, upload its metadata & the file itself
    directory = os.path.dirname(directory_path)
    for dirpath, subdirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(dirpath, filename)
            print(f"Uploading file from {file_path}")
            # upload_midi_file(local_file_path=file_path)   # todo uncomment when ok


def main():
    init_firebase_connexion()

    if len(sys.argv) > 1:
        dir = os.path.dirname(sys.argv[1])
        upload_files_from_dir(dir)
    else:
        raise Exception("No input provided: please provide the path to the directory you wish to process")


if __name__ == '__main__':
    main()
