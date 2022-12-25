from unittest.mock import patch, Mock, call
from queue import Queue
from client import ClientWorker


def test_client_worker():
    with patch("client.socket") as mock:
        socket_mock = Mock()
        socket_mock.connect.return_value = None
        socket_mock.sendall.return_value = None
        socket_mock.recv.return_value = b"result"

        mock.socket.return_value = socket_mock

        q = Queue()
        worker = ClientWorker(q, 8000)
        worker.start()

        q.put("hello")

        q.join()

        q.put(None)

        worker.join()

        assert mock.socket.call_count == 1
        assert socket_mock.connect.call_count == 1
        assert socket_mock.sendall.call_count == 1
        assert socket_mock.recv.call_count == 1
        assert socket_mock.close.call_count == 1

        assert socket_mock.connect.call_args_list == [call(("", 8000))]
        assert socket_mock.sendall.call_args_list == [call(b"hello")]
        assert socket_mock.recv.call_args_list == [call(4096)]
        assert socket_mock.close.call_args_list == [call()]
