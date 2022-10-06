from abc import ABC, abstractmethod


class BaseReader(ABC):
    def __init__(self, fileobj):
        self.file = fileobj
        super().__init__()

    @abstractmethod
    def read(self):
        pass


class BaseWriter(ABC):
    def __init__(self, fileobj):
        self.file = fileobj
        super().__init__()

    @abstractmethod
    def dump(self, data):
        pass
