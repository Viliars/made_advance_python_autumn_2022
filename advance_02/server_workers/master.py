import socket
import queue
from loguru import logger
from .worker import ServerWorker


class Master:
    def __init__(self, workers: int, ktop: int, port: int):
        self.workers = workers
        self.ktop = ktop
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.queue = queue.Queue(100)

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
