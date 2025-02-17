import genanki
import os
import csv
from time import sleep

phrase_en: list[list[str]] = []
phrase_pt: list[list[str]] = []


def file_read(file_name: str) -> list[str]:

    temporary_list: list[str] = []

    with open(file_name, mode='r', encoding='utf-8') as data:
        list_phrases = csv.reader(data)
        for i, row in enumerate(list_phrases):
            temporary_list.append(str(row[0]))

        return temporary_list


phrase_en.append(file_read('en.csv'))
phrase_pt.append(file_read('pt.csv'))


# criação do deck
my_model = genanki.Model(
    54327,
    'Modelo com Áudio',
    fields=[
        {'name': 'front'},
        {'name': 'back'},
        {'name': 'Audio'},
    ],
    templates=[
        {
            'name': 'Card de Frente',
            'qfmt': '<h2>{{front}}</h2><br>{{Audio}}',
            'afmt': '<h2>{{front}}</h2>{{Audio}}<br><h3>{{back}}</h3>',
        },
    ],
    css="h3, h2, br { text-align: center }"
)

deck = genanki.Deck(
    973945,
    'basico anki'
)

folder_audio = 'sons'
list_audios: list[str] = [a for a in os.listdir(
    folder_audio) if a.endswith(('.mp3'))]

file_order: list[str] = sorted(
    list_audios, key=lambda x: int(x.split('audio')[0]))

for i, (en, pt, audio) in enumerate(zip(phrase_en[0], phrase_pt[0], file_order)):

    nota = genanki.Note(
        model=my_model,
        fields=[en, pt, f'[sound:{audio}]']
    )
    # print(audio)

    deck.add_note(nota)

# # busca pelo nome do audio
pack = genanki.Package(deck)


pack.media_files = [os.path.join(folder_audio, audio) for audio in file_order]

print(pack)
sleep(1)
pack.write_to_file('basic02_audio.apkg')

print("Deck criado com sucesso: deck_com_audio")
