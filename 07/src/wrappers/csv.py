import csv
from src.base import BaseReader, BaseWriter


class CsvReader(BaseReader):
    def read(self) -> list[list[str]]:
        return list(csv.reader(self.file))


class CsvWriter(BaseWriter):
    def dump(self, data: list[list[str]]) -> None:
        writer = csv.writer(self.file)
        writer.writerows(data)
