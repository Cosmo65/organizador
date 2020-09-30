import os

DEFAULT_EXTENSIONS = {
    "images": ["png", "jpg", "jpeg", "gif", "bmp"],
    "audios": ["mp3", "wma", "wav"],
    "videos": ["avi", "mp4", "3gp", "mov", "xmv"],
    "docs": ["pdf", "txt", "pps", "ppsx", "ppt", "pptx", "xls", "xlsx", "doc", "docx", ],
    "zips": ["zip", "rar", "7zip"],
}


class OrganizerByExtensions:
    def __init__(self, extensions_map: dict, target_path: str, path: str = "./", topdown: bool = True,
                 others_folder_name: str = "others"):
        self._path = os.path.abspath(path)
        self._topdown = topdown
        self._extensions_map = extensions_map
        self._target_path = os.path.abspath(target_path)
        self._other_folder_name = others_folder_name

        if not os.path.exists(self._path):
            raise NotADirectoryError(f"Do not have a directory on a '{self._path}'")

        if not os.path.exists(self._target_path):
            os.makedirs(self._target_path)

    def start(self):
        for root, folders, files in os.walk(self._path, topdown=self._topdown):
            for file in files:
                self._process_file(f"{root}\\{file}")

    def set_path(self, path):
        if not os.path.exists(os.path.abspath(path)):
            raise NotADirectoryError("The path '{}' does not exists!".format(os.path.abspath(path)))
        self._path = os.path.abspath(path)

    def get_path(self):
        return self._path

    def __repr__(self):
        return f"<OrganizerByExtensions '{self._path}'>"

    @staticmethod
    def _move_file(target_path: str, current_file_path: str):
        target_folder = os.path.split(target_path)[0]
        os.makedirs(target_folder, exist_ok=True)
        os.rename(current_file_path, target_path)

    def _process_file(self, filepath):
        filename = os.path.split(filepath)[1]
        ext = filename.split('.')[-1]

        for key in self._extensions_map:
            if ext in self._extensions_map[key]:
                target = key
                break
        else:
            target = self._other_folder_name

        self._move_file(f"{self._target_path}\\{target}\\{filename}", filepath)
