import json
from src.base import BaseReader, BaseWriter


class JsonReader(BaseReader):
    def read(self) -> dict:
        data = json.load(self.file)
        return data


class JsonWriter(BaseWriter):
    def dump(self, data: dict) -> None:
        json.dump(data, self.file)
