from utils import *
import os


def new_container(file_name):
    # Cut the video
    command_cut = f'ffmpeg -i {file_name} -ss 0 -t 60 -c:v copy -c:a copy cut.mp4'
    os.system(command_cut)

    # Get the audio of the files

    # command_mp3 = f'ffmpeg -i {file} -map a -ac 2 audio.mp3'
    # getting errors with this line, says no mp3 encoder but appears in the list ffmpeg codecs
    command_aac = f'ffmpeg -i {file_name} -vn -b:a 100K audio.aac'
    os.system(command_aac)

    # Put it together in new output
    # command_save = 'ffmpeg -i cut.mp4 -i audio.mp3 -i audio.aac -map 0 -map 1:a -map 2:a -c copy output.mp4'
    command_save = f'ffmpeg -i cut.mp4 -i audio.aac -map 0 -map 1:a -c copy output_1min.mp4'
    os.system(command_save)

    os.remove('cut.mp4')
    os.remove('audio.aac')


file = menu()
new_container(file)
