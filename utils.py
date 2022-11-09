import glob
import os


def menu():
    lof = glob.glob("*.mp4")

    for f in lof:
        print(lof.index(f) + 1, f)

    nof = int(input("Number of file to select: "))

    name = lof[nof - 1]
    print(name)
    print("\n")

    return name


def get_audio_info(file):
    command = f'ffmpeg -i {file} 2> info.txt'
    os.system(command)

    extract_lines = open('info.txt').readlines()

    with open('audio_info.txt', 'w') as audio:
        for line in extract_lines:
            if line.__contains__("Audio"):
                audio.write(line)

    os.remove('info.txt')


def select_task():
    options = ["parser", "new_1min_video", "resize_video", "check_stream_by_audio"]

    for option in options:
        print(options.index(option) + 1, option)

    n = int(input("Choose your task: "))
    print(options[n - 1])
    print("\n")

    return n

