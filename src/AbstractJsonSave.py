from abc import ABC, abstractmethod


class AbstractJsonSave(ABC):

    @abstractmethod
    def save_file(self, data: list):
        pass

    @abstractmethod
    def read_file(self):
        pass