from gtts import gTTS
from playsound import playsound
import os

TEXT_COMMANDS_TO_SPEECH = [
    'Tell me what to grasp',
    'Planning the movement now...',
    'Pick up banana!'
]

OUTPUT_DIR = r'./out'


def generate_audio_file(command: str):
    gTTS(command, lang='pt').save(
        os.path.abspath(os.path.join(
            OUTPUT_DIR, f'{"_".join(command.split()).lower()}.mp3')))


def play_audio_from_file(filename: str):
    playsound(os.path.abspath(os.path.join(OUTPUT_DIR, filename)))


if __name__ == '__main__':
    for command in TEXT_COMMANDS_TO_SPEECH:
        generate_audio_file(command)

    # UNCOMMENT if you want to play the generated audios
    # for file in os.listdir(os.path.abspath(OUTPUT_DIR)):
    #     play_audio_from_file(file)
