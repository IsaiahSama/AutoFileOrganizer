# local.py

import os
import sys
from file_types import file_types

def generic_organize(file_path):
    for file_name in os.listdir(file_path):
        file_ext = os.path.splitext(file_name)[1][1:] # Get the file extension without the dot
        for folder_name, extensions in file_types.items():
            if file_ext in extensions or "*" in extensions:
                folder_path = os.path.join(file_path, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                os.rename(os.path.join(file_path, file_name), os.path.join(folder_path, file_name))
                break

def main():
    if len(sys.argv) != 3:
        print("Usage: python local.py \"folder_path_in_quotes\" level")
        sys.exit(1)

    file_path = sys.argv[1]
    _mode_ = sys.argv[2].lower()

    if not os.path.exists(file_path):
        print(f"The specified path '{file_path}' does not exist.")
        sys.exit(1)

    if _mode_ not in ["generic", "specific"]:
        print("Invalid mode. Mode must be either 'generic' or 'specific'.")
        sys.exit(1)

    if _mode_ == "specific":
        print("The specific functionality is not available as yet. Running generic organization.")

    generic_organize(file_path)

if __name__ == "__main__":
    main()