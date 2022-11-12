from loguru import logger
from .worker import ClientWorker


def chunks(lst: list, n: int) -> list[list]:
    chunk_size = len(lst) // n
    remainder = len(lst) % n

    result = []
    for i in range(0, n):
        result.append(lst[i * chunk_size: (i + 1) * chunk_size])

    for i in range(remainder):
        result[i].append(lst[n * chunk_size + i: n * chunk_size + i + 1])

    return result


class Client:
    def __init__(self, workers: int, filename: str, port: int):
        self.workers = workers
        self.filename = filename
        self.port = port

        with open(filename, "r", encoding="utf-8") as fin:
            self.urls = [line.strip() for line in fin]

        self.batches = chunks(self.urls, self.workers)

    def create_workers(self):
        logger.debug("Create workers")
        self.workers = [
            ClientWorker(self.batches[i], self.port) for i in range(self.workers)
        ]

    def start_workers(self):
        logger.debug("Start workers")
        for worker in self.workers:
            worker.start()

    def join(self):
        logger.debug("Join workers")
        for worker in self.workers:
            worker.join()

    def start_client(self):
        logger.info("Start client")
        self.create_workers()
        self.start_workers()
        self.join()
