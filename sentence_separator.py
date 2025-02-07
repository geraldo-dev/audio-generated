import csv

phrase_en: list[str] = []
phrase_pt: list[str] = []


def sentence_separator(file_name: str) -> None:

    with open(file_name, 'r', encoding='utf-8') as file:
        files_text: str = file.read()
        list_text: list[str] = files_text.replace('\n', ';').split(';')

        for i in range(len(list_text)):
            if i % 2 == 0:

                phrase_en.append(list_text[i])
            else:
                if i % 2 != 0:
                    phrase_pt.append(list_text[i])


def file_save(file_name: str, list_phrases: list[str]):

    with open(file_name, 'a', encoding='utf-8') as data:
        for i in list_phrases:
            data.write(i+'\n')
        print('salvo')


sentence_separator('ingles-Portugues.csv')
file_save('en.csv', phrase_en)
file_save('pt.csv', phrase_pt)
