"""
Scripts for editing the Firebase database
"""
import os
import sys
from database.metadata_processing import *
from database.firestore import *
import re


def format_file_name(file_name: str) -> str:
    file_name = file_name[:-4]  # remove extension first -> todo check if there are .midi files instead of .mid

    print(f"--- file name: {file_name}")
    if len(re.findall('\\.', file_name)) > 1:
        print(f"WARNING: using format_string on a file name containing dots! ({file_name})", file=sys.stderr)
        formatted_name = re.sub(".mid", "", file_name)
        print(f"file name before . subs: {formatted_name}")
        formatted_name = re.sub("\\.", "_", formatted_name)
        print(f"file name after . subs: {formatted_name}")
        formatted_name = format_string(formatted_name)
    else:
        formatted_name = format_string(str(file_name).split('.')[0])
    return f"{formatted_name}.mid"


def get_formatted_file_path(file_path: str) -> str:
    """
    Only format the file name, then return the whole path with the new file name
    Args:
        file_path: The path to format

    Returns: The formatted file path

    """

    # print(f"input path: {file_path}")
    path_to_file_dir = os.path.abspath(os.path.dirname(file_path))
    file_name = os.path.basename(file_path)

    formatted_name = format_file_name(file_name)
    return os.path.join(path_to_file_dir, formatted_name)


def rename_files_in_dir(directory_path: str):
    directory = os.path.dirname(directory_path)

    for dirpath, subdirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.normpath(os.path.join(dirpath, filename))
            new_file_path = get_formatted_file_path(file_path)
            print(f">> renaming {file_path} --->>> {new_file_path}")
            os.rename(file_path, new_file_path)  # rename your file   # todo uncomment when ok


def process_files_from_dir(directory_path: str):

    directory = os.path.abspath(os.path.dirname(directory_path))
    # rename files to a correct format
    print(f">>> Renaming files in {directory}")
    # rename_files_in_dir(directory_path)

    # file by file, upload its metadata & the file itself
    for dirpath, subdirs, files in os.walk(directory):
        for filename in files:
            print(f"> Current file name: {filename}")
            file_path = os.path.join(dirpath, filename)
            # print(f"Uploading file from {file_path}")
            # todo upload the file in its artist's folder
            # upload_midi_file(local_file_path=file_path)   # todo uncomment when ok


def main():
    # init_firebase_connexion()     # todo uncomment when ready

    if len(sys.argv) > 1:
        input_path = sys.argv[1]
        if input_path[-1] != "/":
            input_path += "/"

        dirname = os.path.dirname(__file__)
        dir = os.path.join(dirname, input_path)
        process_files_from_dir(dir)

    else:
        raise Exception("No input provided: please provide the path to the directory you wish to process")


if __name__ == '__main__':
    main()
