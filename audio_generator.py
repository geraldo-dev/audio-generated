from gtts import gTTS
import re
import csv
from time import sleep


all_texts: list[str] = []

with open('lista_frases_ingles.csv', mode='r', encoding='utf-8') as file:
    read_file = csv.reader(file)
    for row in read_file:
        all_texts.append(row[0])

print(all_texts)

sleep(2)


def audio_generator(texts: list[str], lang: str = 'en', slow: bool = True) -> None:

    for text in texts:
        print(f"{text}")
        tts = gTTS(text=text, lang=lang, slow=slow)

        name_file: str = re.sub(
            r'[<>:"/\\|?*]', '', text.replace(' ', '_'))

        tts.save(f'./audio/{name_file}.mp3')

    print('save')


audio_generator(all_texts)
