import argparse
from threading import Thread
from urllib import request
from queue import Queue
import json
from collections import Counter
import socket
import logging
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
)

logger = logging.getLogger(__name__)


counter = 0


class ServerWorker(Thread):
    def __init__(self, queue: Queue, k: int):
        Thread.__init__(self)

        self.queue = queue
        self.k = k

    def run(self):
        logger.debug("Run Server Worker")

        while True:
            client_socket = self.queue.get()

            if client_socket is None:
                break

            try:
                client_request = self.read_client_request(client_socket)

                if client_request:
                    url = client_request.decode(encoding="utf-8")
                    answer = self.parse_url(url)

                    client_socket.sendall(bytes(answer, encoding="utf-8"))

                    global counter
                    counter += 1
                    print(f"Сервер обработал {counter} urls.")
                else:
                    logger.error("Bad request")
            except Exception as e:
                logger.error(e)
            finally:
                self.queue.task_done()

    def read_client_request(self, client_socket: socket) -> bytes:
        try:
            client_request = client_socket.recv(1024)
            return client_request
        except ConnectionResetError:
            return None

    def parse_url(self, url: str) -> str:
        try:
            with request.urlopen(url) as response:
                text = response.read().decode(encoding="utf-8")
            parser = BeautifulSoup(text, features="html.parser")

            return self.get_top_k(parser.get_text())
        except Exception as exc:
            logger.error("Error while parse url")
            return json.dumps({"error": str(exc)})

    def get_top_k(self, text: str) -> str:
        result_dict = {}
        for word, count in Counter(text.split()).most_common(self.k):
            result_dict[word] = count
        return json.dumps(result_dict)


class Master:
    def __init__(self, workers: int, ktop: int, port: int):
        self.workers = workers
        self.ktop = ktop
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.queue = Queue(self.workers)

    def bind_socket(self):
        self.sock.bind(("", self.port))
        self.sock.listen()

    def create_workers(self):
        logger.debug("Create workers")
        self.workers = [
            ServerWorker(self.queue, self.ktop) for _ in range(self.workers)
        ]

    def start_workers(self):
        logger.debug("Start workers")
        for worker in self.workers:
            worker.start()

    def start_server(self):
        logger.info("Start server")
        self.create_workers()
        self.start_workers()
        self.bind_socket()

        while True:
            client_socket, _ = self.sock.accept()

            client_socket.setblocking(False)

            self.queue.put(client_socket)


def main():
    logger.info("Starting server")
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--workers", type=int, help="Workers count")
    parser.add_argument(
        "-k", "--ktop", type=int, help="The number of most frequent words"
    )
    parser.add_argument("-p", "--port", type=int, default=8000, help="Server port")

    args = parser.parse_args()

    server = Master(args.workers, args.ktop, args.port)

    server.start_server()


if __name__ == "__main__":
    main()
