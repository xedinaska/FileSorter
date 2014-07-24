from os import listdir
import os.path
import shutil


class Sorter:

    SORTED_FOLDER_NAME = 'SORTED'

    DIRECTORY_PATH = '/Users/Xedin/Documents'
    SORTED_PATH = DIRECTORY_PATH + '/' + SORTED_FOLDER_NAME

    MUSIC_FOLDER = 'MUSIC'
    IMAGES_FOLDER = 'IMAGES'
    VIDEO_FOLDER = 'VIDEO'
    TEXT_FOLDER = 'TEXT'
    ARCHIVES_FOLDER = 'ARCHIVES'
    SOFT_FOLDER = 'SOFT'
    ETC_FOLDER = 'ETC'

    FOLDERS_LIST = [MUSIC_FOLDER, IMAGES_FOLDER, VIDEO_FOLDER, TEXT_FOLDER, ARCHIVES_FOLDER, SOFT_FOLDER, ETC_FOLDER]

    EXTENSION_PATHS = {
        'mp3': MUSIC_FOLDER,
        'flac': MUSIC_FOLDER,
        'm3u': MUSIC_FOLDER,
        'txt': TEXT_FOLDER,
        'pdf': TEXT_FOLDER,
        'doc': TEXT_FOLDER,
        'docx': TEXT_FOLDER,
        'xls': TEXT_FOLDER,
        'xlsx': TEXT_FOLDER,
        'jpg': IMAGES_FOLDER,
        'png': IMAGES_FOLDER,
        'jpeg': IMAGES_FOLDER,
        'ico': IMAGES_FOLDER,
        'mp4': VIDEO_FOLDER,
        'avi': VIDEO_FOLDER,
        'zip': ARCHIVES_FOLDER,
        'rar': ARCHIVES_FOLDER,
        'exe': SOFT_FOLDER,
        'dmg': SOFT_FOLDER
    }

    def __init__(self):
        self._create_base_folders()

    def sort_files(self):
        self._start_sort_process()

    def _start_sort_process(self):
        dir_files = listdir(self.DIRECTORY_PATH)

        for filename in dir_files:
            if filename != self.SORTED_FOLDER_NAME:
                ext = os.path.splitext(filename)[1][1:]
                try:
                    folder_to_move = self.EXTENSION_PATHS[ext]
                except KeyError:
                    folder_to_move = self.ETC_FOLDER

                self._move_file(filename, folder_to_move)

    def _move_file(self, filename, folder):
        file_from_path = self.DIRECTORY_PATH + '/' + filename
        file_to_path = self.SORTED_PATH + '/' + folder
        shutil.move(file_from_path, file_to_path)
        print('Moved ' + filename + ' from ' + file_from_path + ' to ' + file_to_path)

    def _create_base_folders(self):

        if not os.path.exists(self.SORTED_PATH):
                os.makedirs(self.SORTED_PATH)

        for folder_name in self.FOLDERS_LIST:
            folder_path = self.SORTED_PATH + '/' + folder_name

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

sorter = Sorter()
sorter.sort_files()
