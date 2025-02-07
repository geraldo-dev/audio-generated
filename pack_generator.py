import genanki
import os
import csv

phrase_en: list[list[str]] = []
phrase_pt: list[list[str]] = []


def file_read(file_name: str) -> list[str]:

    temporary_list: list[str] = []

    with open(file_name, mode='r', encoding='utf-8') as data:
        list_phrases = csv.reader(data)
        for i, row in enumerate(list_phrases):
            if i < 100:
                temporary_list.append(str(row[0]))

        return temporary_list


phrase_en.append(file_read('en.csv'))
phrase_pt.append(file_read('pt.csv'))


# criação do deck
my_model = genanki.Model(
    1234567890,
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
    123456789,
    'basico anki 100'
)

folder_audio = 'sons'

for i, (en, pt) in enumerate(zip(phrase_en[0], phrase_pt[0])):
    nota = genanki.Note(
        model=my_model,
        fields=[en, pt, f'[sound:{en}.mp3]']
    )

    deck.add_note(nota)

# # busca pelo nome do audio
pack = genanki.Package(deck)

list_audios: list[str] = [a for a in os.listdir(
    folder_audio) if a.endswith(('.mp3'))]

pack.media_files = [os.path.join(folder_audio, x) for x in list_audios]

pack.write_to_file('deck_com_audio.apkg')

print("Deck criado com sucesso: deck_com_audio")
