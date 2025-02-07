import re
from gtts import gTTS
import csv


def audio_generator(file_name: str, slow: bool = True, folder: str = 'sons') -> None:
    pattern = r"'[\/|.,?;><\$@`´\-]"

    with open(file_name, mode='r', encoding='utf-8') as data:

        read_file = csv.reader(data)

        for i, row in enumerate(read_file):
            if i < 100:
                text: str = row[0]
                tts = gTTS(text, lang='en', slow=slow)
                text = re.sub(pattern, '', text)
                name_text = text.replace("?", '')
                tts.save(f'./{folder}/{name_text.replace(' ', '')}.mp3')


audio_generator(file_name='en.csv', slow=True, folder='sons')
print('music save')
