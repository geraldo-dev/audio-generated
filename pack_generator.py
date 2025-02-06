
import genanki
import os

# Cria um modelo de card básico com suporte a áudio
modelo = genanki.Model(
    1234567890,  # ID único
    'Modelo com Áudio',
    fields=[
        {'name': 'Texto'},
        {'name': 'Audio'},
    ],
    templates=[
        {
            'name': 'Card de Frente',
            'qfmt': '<h2>{{Texto}}</h2><br>{{Audio}}',  # Frente do cartão
            # Resposta (inclui o áudio)
            'afmt': '<h2>{{Texto}}</h2><br>{{Audio}}',
        },
    ],
)

# Cria um deck com um ID único
deck = genanki.Deck(
    123456789,  # ID único
    'Deck com Áudio'
)

# Caminho para os arquivos de áudio
pasta_audio = 'audio'

# Itera pelos arquivos de áudio na pasta
for arquivo in os.listdir(pasta_audio):
    if arquivo.endswith(('.mp3', '.wav')):
        # Usa o nome do arquivo como texto
        texto = os.path.splitext(arquivo)[0].replace('_', ' ')
        # Formato esperado pelo Anki para áudio
        caminho_audio = f'[sound:{arquivo}]'

        # Cria uma nota (card)
        nota = genanki.Note(
            model=modelo,
            fields=[texto, caminho_audio]
        )

        # Adiciona a nota ao deck
        deck.add_note(nota)

# Cria um pacote e inclui os arquivos de áudio
pacote = genanki.Package(deck)
pacote.media_files = [os.path.join(pasta_audio, f) for f in os.listdir(
    pasta_audio) if f.endswith(('.mp3', '.wav'))]

# Exporta o deck para um arquivo .apkg
pacote.write_to_file('deck_com_audio.apkg')

print("Deck criado com sucesso: deck_com_audio.apkg")
