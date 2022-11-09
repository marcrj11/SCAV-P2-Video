from utils import *
import os


def parser(file_name):
    # Apply transformation using ffmpeg
    command = f'ffmpeg -i {file_name} 2> info_about_file.txt'
    os.system(command)

    extract_lines = open('info_about_file.txt').readlines()

    with open('new_info.txt', 'w') as new_container:
        for line in extract_lines:
            if line.__contains__("title") or line.__contains__("Duration") or line.__contains__("Stream"):
                new_container.write(line)

    os.remove('info_about_file.txt')


# Select video to apply transformation
file = menu()
parser(file)
