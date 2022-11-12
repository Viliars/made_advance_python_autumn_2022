from threading import Thread
import socket
import json
from loguru import logger


class ClientWorker(Thread):
    def __init__(self, urls: list[str], port: int):
        Thread.__init__(self)

        self.urls = urls
        self.port = port

    def run(self):
        logger.debug("Run client worker")
        for url in self.urls:
            while True:
                try:
                    logger.info(f"Клиент отправил серверу: {url}")
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client_socket.connect(("", self.port))
                    byte_url = bytes(url, encoding="utf-8")
                    client_socket.sendall(byte_url)
                    data = client_socket.recv(4096)
                except socket.error:
                    logger.info("Сервер оборвал соединение")
                else:
                    print(url, json.loads(data.decode("utf-8")))
                    client_socket.close()
                    break
