import os
from datetime import date


class OrganizerByDate:
    def __init__(self, current_dir: str = os.getcwd(), target_dir: str = './'):
        self._current_dir = os.path.abspath(current_dir)
        self._target_dir = os.path.abspath(target_dir)

    def start(self):
        """
        Função responsavel pelo start do processo de discovering e pela chamada do processamento
        """
        for root, folders, file in os.walk(self._current_dir, topdown=True):
            self._process((root, folders, file))

    def _process(self, info: tuple):
        """
        Função responsavel pelo rocessamento dos arquivos,


        param info:
        """
        root = info[0]
        files = info[2]
        for file in files:
            file_path = f"{root}\\{file}"
            folder_name = str(date.fromtimestamp(os.path.getmtime(file_path)))
            target_folder_path = f"{self._target_dir}\\{folder_name}"
            if not os.path.exists(target_folder_path):
                os.mkdir(f"{target_folder_path}")
            self._move_file(file_path, f"{target_folder_path}\\{file}")

    @staticmethod
    def _move_file(current_file_path: str, target_path: str):
        os.rename(current_file_path, target_path)
