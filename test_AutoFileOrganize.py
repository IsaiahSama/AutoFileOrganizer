# test_AutoFileOrganize.py

import os
import sys
from file_types import file_types
from autoFileOrganize import generic_organize

def create_test_files():
    test_folder = "TestingFileOrganize"
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)

    for folder_name, extensions in file_types.items():
        for ext in extensions:
            if (ext == "*"): continue
            for i in range(5):
                file_name = f"test{i}.{ext}"
                file_path = os.path.join(test_folder, file_name)
                with open(file_path, 'w') as file:
                    file.write(f"This is a test file for {ext} extension.")

def main():
    create_test_files()
    input("Press enter to organize files...")

    test_folder = "TestingFileOrganize"
    if os.path.exists(test_folder):
        generic_organize(test_folder)
    else:
        print(f"The folder '{test_folder}' does not exist.")

if __name__ == "__main__":
    main()