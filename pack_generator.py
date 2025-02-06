import genanki
import os
import csv

phrase_en: list[str] = []
phrase_pt: list[str] = []

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
    'Deck com Áudio'
)

folder_audio = 'sons'

for file in os.listdir(folder_audio):
    count: int = 0
    if file.endswith(('.mp3', '.wav')):

        path_audio = f'[sound:{file}]'

        nota = genanki.Note(
            model=my_model,
            fields=[str(phrase_en[count]), str(phrase_pt[count]), path_audio]
        )
        count = count + 1
        deck.add_note(nota)

pack = genanki.Package(deck)
pack.media_files = [os.path.join(folder_audio, f) for f in os.listdir(
    folder_audio) if f.endswith(('.mp3', '.wav'))]

pack.write_to_file('deck_com_audio.apkg')

print("Deck criado com sucesso: deck_com_audio.apkg")
