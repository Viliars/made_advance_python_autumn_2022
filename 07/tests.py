import unittest
from io import StringIO
from src.wrappers.txt import TxtReader, TxtWriter
from src.wrappers.json import JsonReader, JsonWriter
from src.wrappers.csv import CsvReader, CsvWriter
from src.functions import filtered_file, dump_data, read_data


class TestTxt(unittest.TestCase):
    def test_read(self):
        fileobj = StringIO("hello\njson\ncsv\ntxt\n")

        obj = TxtReader(fileobj)
        data = obj.read()

        self.assertEqual(data, ["hello", "json", "csv", "txt"])

    def test_dump(self):
        fileobj = StringIO()
        lines = ["hello", "json", "csv", "txt"]
        obj = TxtWriter(fileobj)

        obj.dump(lines)

        self.assertEqual(fileobj.getvalue(), "hello\njson\ncsv\ntxt\n")


class TestJson(unittest.TestCase):
    def test_read(self):
        fileobj = StringIO("""[
            {"x": 1},
            {"y": 2}
        ]""")

        obj = JsonReader(fileobj)
        data = obj.read()

        self.assertEqual(data, [
            {'x': 1},
            {'y': 2}
        ])

    def test_dump(self):
        fileobj = StringIO()
        data = ["hello", "json", "csv", "txt"]
        obj = JsonWriter(fileobj)

        obj.dump(data)

        self.assertEqual(fileobj.getvalue(), '["hello", "json", "csv", "txt"]')

        fileobj = StringIO()
        data = {"x": {"y": 2}}
        obj = JsonWriter(fileobj)

        obj.dump(data)

        self.assertEqual(fileobj.getvalue(), '{"x": {"y": 2}}')


class TestCsv(unittest.TestCase):
    def test_read(self):
        fileobj = StringIO("bla1,bla2,bla3,ID1\r\nbla4,bla5,bla6,ID2\r\n")

        obj = CsvReader(fileobj)
        data = obj.read()

        self.assertEqual(data, [["bla1", "bla2", "bla3", "ID1"],
                                ["bla4", "bla5", "bla6", "ID2"]])

    def test_dump(self):
        fileobj = StringIO()
        lines = [["hello", "json", "csv", "txt"], ["xml"]]
        obj = CsvWriter(fileobj)

        obj.dump(lines)

        self.assertEqual(fileobj.getvalue(), "hello,json,csv,txt\r\nxml\r\n")


class TestFunctions(unittest.TestCase):
    def test_integrations_1(self):
        fileobj = StringIO()

        dump_data({"x": "1"}, fileobj, writer=JsonWriter)

        fileobj.seek(0)

        data = read_data(fileobj, reader=JsonReader)
        self.assertEqual(data, {"x": "1"})

    def test_integration_2(self):
        fileobj = StringIO()

        dump_data(["hello"], fileobj, writer=TxtWriter)

        fileobj.seek(0)

        data = read_data(fileobj, reader=TxtReader)
        self.assertEqual(data, ["hello"])

    def test_integration_3(self):
        fileobj = StringIO()

        dump_data([["hello"]], fileobj, writer=CsvWriter)

        fileobj.seek(0)

        data = read_data(fileobj, reader=CsvReader)
        self.assertEqual(data, [["hello"]])


class TestFilter(unittest.TestCase):
    def test_filter(self):
        fileobj = StringIO("hello my name\nis Michael\nBlaBLA\nhello world\nnono cat\n")

        result = list(filtered_file(fileobj, ["my", "blabla", "world"]))

        self.assertEqual(result, ['hello my name', 'BlaBLA', 'hello world'])

        fileobj.seek(0)

        result = list(filtered_file(fileobj, ["nono", "is", "bla"]))

        self.assertEqual(result, ['is Michael', 'nono cat'])
