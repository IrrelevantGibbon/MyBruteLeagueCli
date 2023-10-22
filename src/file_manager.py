import pickle
import os
from typing import TypeVar

T = TypeVar("T")


class FileManager:
    def __init__(self):
        self.default_folder = "datas/"

        if not os.path.exists(self.default_folder):
            os.makedirs(self.default_folder)

    def read_file(self, filename: str) -> T:
        with open(self.default_folder + filename, "rb") as f:
            return pickle.load(f)

    def write_file(self, filename: str, data: T) -> None:
        with open(self.default_folder + filename, "wb") as f:
            pickle.dump(data, f)

    def delete_file(self, filename: str) -> None:
        os.remove(self.default_folder + filename)

    def list_files(self) -> list[str]:
        return os.listdir(self.default_folder)
