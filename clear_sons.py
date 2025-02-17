from ntpath import isfile
import os
folder_path_csv = 'C:\\Users\\GERALDO\\Documents\\audio-generated'
folder_path_music = 'C:\\Users\\GERALDO\\Documents\\audio-generated\\sons'


def remover_files(folder_path: str, format: str = '.mp3'):
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):

            path_file = os.path.join(folder_path, file)
            if os.path.isfile(path_file) and file.lower().endswith(".mp3"):
                os.remove(path_file)

        if not os.listdir(folder_path):
            print('pasta vazia')
    else:
        print('não existe')


remover_files(folder_path_music, '.mp3')
remover_files(folder_path_csv, '.csv')
