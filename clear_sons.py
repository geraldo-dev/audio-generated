from ntpath import isfile
import os


def remover_sons():
    folder_path = 'C:\\Users\\GERALDO\\Documents\\audio-generated\\sons'

    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):

            path_file = os.path.join(folder_path, file)
            if os.path.isfile(path_file) and file.lower().endswith(".mp3"):
                os.remove(path_file)

        if not os.listdir(folder_path):
            print('pasta vazia')
    else:
        print('não existe')
    # remover en.csv, pt.csv


remover_sons()
