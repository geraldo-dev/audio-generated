from gtts import gTTS
import csv


def audio_generator(file_name: str, slow: bool = True, folder: str = 'sons') -> None:

    with open(file=file_name, mode='r', encoding='utf-8') as data:

        read_file = csv.reader(csvfile=data)

        for i, row in enumerate(read_file):
            if i < 100:
                text: str = row[0]
                tts = gTTS(text=text, lang='en', slow=slow)
                tts.save(f'./{folder}/{i}_phrases.mp3')


audio_generator(file_name='en.csv', slow=True, folder='sons')
print('music save')
