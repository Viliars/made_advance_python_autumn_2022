from threading import Thread
from socket import socket
from urllib import request
from queue import Queue
import json
from collections import Counter
from bs4 import BeautifulSoup
from loguru import logger


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
