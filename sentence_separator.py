import csv


phrase_en: list[str] = []
phrase_pt: list[str] = []


def sentence_separator(file_name: str) -> None:

    with open(file_name, 'r', newline='', encoding='utf-8') as file:

        files_text = csv.reader(file, delimiter=';')
        i: int = 0
        for row in files_text:

            if i < 99:
                phrase_en.append(row[0])
                phrase_pt.append(row[1])


def file_save(file_name: str, list_phrases: list[str]):

    with open(file_name, 'w', newline='', encoding='utf-8') as data:
        for i in list_phrases:
            data.write(i+'\n')


sentence_separator('ingles-Portugues.csv')

file_save('en.csv', phrase_en)
file_save('pt.csv', phrase_pt)
print('salvo')
