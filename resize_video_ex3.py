import os
from utils import *


def resize_video(file_name):
    valid = False

    while not valid:
        w = input('Choose the width you want to resize your file(must be multiple of 2): ')
        h = input('Choose the height you want to resize your file(must be multiple of 2): ')

        if int(w) > 0 and int(h) > 0 and int(w) % 2 == 0 and int(h) % 2 == 0:
            valid = True
        else:
            print("The resolution desired is not valid, try with other values")

    command = f'ffmpeg -i {file_name} -vf scale={w}:{h} resized_video.mp4'
    os.system(command)


file = menu()
resize_video(file)
