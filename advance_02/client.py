import argparse
from threading import Thread
import socket
import json
from queue import Queue, Empty
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
)

logger = logging.getLogger(__name__)


class ClientWorker(Thread):
    def __init__(self, queue: Queue, port: int):
        Thread.__init__(self)

        self.queue = queue
        self.port = port

    def run(self):
        logger.debug("Run client worker")

        while True:
            try:
                url = self.queue.get(timeout=1)
            except Empty:
                continue

            if url is None:
                break

            try:
                logger.info(f"Клиент отправил серверу: {url}")
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect(("", self.port))
                byte_url = bytes(url, encoding="utf-8")
                client_socket.sendall(byte_url)
                data = client_socket.recv(4096)
                print(url, json.loads(data.decode("utf-8")))
            except Exception as e:
                logger.error(e)
            finally:
                self.queue.task_done()
                client_socket.close()


class Client:
    def __init__(self, workers_count: int, filename: str, port: int):
        self.workers_count = workers_count
        self.filename = filename
        self.port = port
        self.queue = Queue(self.workers_count)
        self.workers = []

    def create_workers(self):
        logger.debug("Create workers")
        self.workers = [
            ClientWorker(self.queue, self.port) for _ in range(self.workers_count)
        ]

    def start_workers(self):
        logger.debug("Start workers")
        for worker in self.workers:
            worker.start()

    def load_urls(self):
        with open(self.filename, "r", encoding="utf-8") as fin:
            for line in fin:
                self.queue.put(line.strip())

    def join(self):
        self.queue.join()

        for _ in self.workers:
            self.queue.put(None)

        logger.debug("Join workers")

        for worker in self.workers:
            worker.join()

    def start_client(self):
        logger.info("Start client")
        self.create_workers()
        self.start_workers()
        self.load_urls()
        self.join()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("workers", type=int, help="Workers count")
    parser.add_argument("filename", type=str, help="File with urls")
    parser.add_argument("-p", "--port", type=int, default=8000, help="Server port")

    args = parser.parse_args()

    client = Client(args.workers, args.filename, args.port)

    client.start_client()


if __name__ == "__main__":
    main()
