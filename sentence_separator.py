import csv

phrase_en: list[str] = []
phrase_pt: list[str] = []

with open('Inglês-Português.csv', 'r', encoding='utf-8') as file:
    texts: str = file.read()
    text_enghlis: list[str] = texts.replace('\n', ';').split(';')

    for i in range(len(text_enghlis)):
        if i % 2 == 0:

            phrase_en.append(text_enghlis[i])
        else:
            if i % 2 != 0:
                phrase_pt.append(text_enghlis[i])


def sentence_separator(file_name: str, list_phrases: list[str]):

    with open(file_name, 'a', encoding='utf-8') as data:
        for i in list_phrases:
            data.write(i+'\n')
        print('salvo')


sentence_separator('en.csv', phrase_en)
sentence_separator('pt.csv', phrase_pt)
