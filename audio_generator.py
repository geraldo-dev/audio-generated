from gtts import gTTS
import csv


def audio_generator(file_name: str, slow: bool = True, folder: str = 'sons', size: int = 100) -> None:

    with open(file_name, mode='r', encoding='utf-8') as data:

        read_file = csv.reader(data)

        for i, row in enumerate(read_file):
            if i < size:
                text: str = row[0]
                tts = gTTS(text, lang='en', slow=slow)
                tts.save(f'./{folder}/{i}audio.mp3')


audio_generator(file_name='en.csv', slow=True, folder='sons', size=296)
print('music save')
