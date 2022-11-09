from utils import *


class Lab2:
    file_name = menu()
    desired_task = select_task()

    def parser_lab2(self):
        # Apply transformation using ffmpeg
        command = f'ffmpeg -i {self.file_name} 2> info_about_file.txt'
        os.system(command)

        extract_lines = open('info_about_file.txt').readlines()

        with open('new_info.txt', 'w') as new_container:
            for line in extract_lines:
                if line.__contains__("title") or line.__contains__("Duration") or line.__contains__("Stream"):
                    new_container.write(line)

        os.remove('info_about_file.txt')

    def new_container_lab2(self):

        # Cut the video
        command_cut = f'ffmpeg -i {self.file_name} -ss 0 -t 60 -c:v copy -c:a copy cut.mp4'
        os.system(command_cut)

        # Get the audio of the files

        # command_mp3 = f'ffmpeg -i {file} -map a -ac 2 audio.mp3'
        # getting errors with this line, says no mp3 encoder but appears in the list ffmpeg codecs
        command_aac = f'ffmpeg -i {self.file_name} -vn -b:a 100K audio.aac'
        os.system(command_aac)

        # Put it together in new output
        # command_save = 'ffmpeg -i cut.mp4 -i audio.mp3 -i audio.aac -map 0 -map 1:a -map 2:a -c copy output.mp4'
        command_save = f'ffmpeg -i cut.mp4 -i audio.aac -map 0 -map 1:a -c copy output_1min.mp4'
        os.system(command_save)

        os.remove('cut.mp4')
        os.remove('audio.aac')

    def resizer_lab2(self):
        valid = False

        while not valid:
            w = input('Choose the width you want to resize your file(must be multiple of 2): ')
            h = input('Choose the height you want to resize your file(must be multiple of 2): ')

            if int(w) > 0 and int(h) > 0 and int(w) % 2 == 0 and int(h) % 2 == 0:
                valid = True
            else:
                print("The resolution desired is not valid, try with other values")

        command = f'ffmpeg -i {self.file_name} -vf scale={w}:{h} resized_video.mp4'
        os.system(command)

    def check_audio_lab2(self):
        get_audio_info(self.file_name)

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

    def run_task(self):

        if self.desired_task == 1:
            self.parser_lab2()

        if self.desired_task == 2:
            self.new_container_lab2()

        if self.desired_task == 3:
            self.resizer_lab2()

        if self.desired_task == 4:
            self.check_audio_lab2()


# LAB 2 TESTER
test = Lab2()
test.run_task()
