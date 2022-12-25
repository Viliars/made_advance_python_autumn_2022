from unittest.mock import patch, Mock, call
from queue import Queue
from server import ServerWorker


def test_server_worker():
    with patch("server.request.urlopen") as mock:
        mock.return_value.__enter__.return_value.read.return_value = b"test test"

        socket_mock = Mock()
        socket_mock.sendall.return_value = None
        socket_mock.recv.return_value = b"result"

        q = Queue()
        worker = ServerWorker(q, 10)
        worker.start()

        q.put(socket_mock)

        q.join()

        q.put(None)

        worker.join()

        assert mock.call_count == 1

        assert socket_mock.sendall.call_count == 1
        assert socket_mock.recv.call_count == 1

        assert socket_mock.sendall.call_args_list == [call(b'{"test": 2}')]
        assert socket_mock.recv.call_args_list == [call(1024)]
