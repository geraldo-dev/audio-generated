import csv


phrase_en: list[str] = []
phrase_pt: list[str] = []


def sentence_separator(file_name: str) -> None:

    with open(file_name, 'r', newline='', encoding='utf-8') as file:

        files_text = csv.reader(file, delimiter=';')

        for row in files_text:

            phrase_en.append(row[0])
            phrase_pt.append(row[1])


def file_save(file_name: str, list_phrases: list[str]):

    with open(file_name, 'w', newline='', encoding='utf-8') as data:
        for i in list_phrases:
            data.write(i+'\n')


sentence_separator('400_frases_ingles_portugues.csv')

file_save('en.csv', phrase_en)
file_save('pt.csv', phrase_pt)
print('salvo')
