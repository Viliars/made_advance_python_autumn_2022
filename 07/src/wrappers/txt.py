from src.base import BaseReader, BaseWriter


class TxtReader(BaseReader):
    def read(self) -> list[str]:
        lines = [line.strip() for line in self.file.readlines()]
        return lines


class TxtWriter(BaseWriter):
    def dump(self, data: list[str]) -> None:
        for line in data:
            self.file.write(line)
            self.file.write('\n')
