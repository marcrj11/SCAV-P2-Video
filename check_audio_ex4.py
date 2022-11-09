import os
from utils import *


def check_audio(file_name):
    get_audio_info(file_name)

    with open('audio_info.txt', 'r') as audio_info:
        for line in audio_info:

            # DTMB uses DRA as audio coder
            if line.__contains__(" dra "):
                print(line)
                print("The broadcasting standard must be DTMB.")

            # ISDB only works with AAC
            elif line.__contains__(" aac "):
                print(line)
                print("The broadcasting standard can be DVB, ISDB or DTMB.")

            # ATSC only works with AC-3
            elif line.__contains__(" ac3 "):
                print(line)
                print("The broadcasting standard can be DVB, ATSC or DTMB.")

            else:
                print(line)
                print("The broadcasting standard must be DVB, or DTMB or couldn't be defined")

    os.remove('audio_info.txt')


file = menu()
check_audio(file)
