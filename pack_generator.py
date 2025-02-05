import genanki
# import os

# modelo de cards
my_model = genanki.Model(
    1234567890,
    'Modelo com Audio',
    fields=[
        {'name': 'Pergunta'},
        {'name': 'Resposta'},
        {'name': 'Audio'},
    ],
    templates=[
        {
            'name': 'card de frente',
            'qfmt': '{{Pergunta}}<br>{{Audio}}',
            'afmt': '{{FrontSide}} {{Resposta}}',
        },
    ])

# crio nome do deck
my_deck = genanki.Deck(123456789, 'Deck com Àudio')

my_note = genanki.Note(
    model=my_model,
    fields=['i am fine, and you ?', ' ', '[sound:i_am_fine_and_you_.mp3]'])

my_deck.add_note(my_note)

package = genanki.Package(my_deck)
package.media_files = ['i_am_fine_and_you_.mp3']
package.write_to_file('./teste_deck.apkg')
