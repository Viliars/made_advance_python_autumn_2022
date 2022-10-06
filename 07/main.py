from abc import ABC, abstractmethod
import json
import csv


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


class TxtReader(BaseReader):
    def read(self) -> list[str]:
        lines = [line.strip() for line in self.file.readlines()]
        return lines


class TxtWriter(BaseWriter):
    def dump(self, data: list[str]) -> None:
        for line in data:
            self.file.write(line)
            self.file.write('\n')


class JsonReader(BaseReader):
    def read(self) -> dict:
        data = json.load(self.file)
        return data


class JsonWriter(BaseWriter):
    def dump(self, data: dict) -> None:
        json.dump(data, self.file)


class CsvReader(BaseReader):
    def read(self) -> list[list[str]]:
        return list(csv.reader(self.file))


class CsvWriter(BaseWriter):
    def dump(self, data: list[list[str]]) -> None:
        writer = csv.writer(self.file)
        writer.writerows(data)


# использование
def read_data(fileobj, reader=TxtReader):
    reader_object = reader(fileobj)
    return reader_object.read()


def dump_data(data, fileobj, writer=TxtWriter):
    writer_object = writer(fileobj)
    writer_object.dump(data)


def filtered_file(fileobj, words):
    words_set = set(words)
    while True:
        line = fileobj.readline().strip()
        if len(line) == 0:
            break
        if len(words_set & set(line.lower().split())):
            yield line
