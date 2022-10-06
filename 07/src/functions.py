from src.wrappers.txt import TxtReader, TxtWriter


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
