import unittest
import subprocess
from time import sleep
from tempfile import NamedTemporaryFile


class TestClientServer(unittest.TestCase):
    def test_1(self):
        input_file = NamedTemporaryFile()
        output_file = NamedTemporaryFile()

        with open(input_file.name, "w", encoding="utf-8") as fout:
            print("http://localhost:7979/python.html", file=fout)

        client_fout = open(output_file.name, "w", encoding="utf-8")

        file_server = subprocess.Popen(
            ["python3", "-m", "http.server", "-d", "tests/", "7979"]
        )

        server = subprocess.Popen(
            ["python3", "server.py", "-w", "1", "-k", "1", "--port", "8999"]
        )

        sleep(1)

        client = subprocess.Popen(
            ["python3", "client.py", "1", input_file.name, "--p", "8999"],
            stdout=client_fout,
        )

        client.wait()
        server.kill()
        file_server.kill()

        server.wait()
        file_server.wait()

        client_fout.close()

        with open(output_file.name, "r", encoding="utf-8") as fin:
            result = fin.read()

        self.assertEqual(result, "http://localhost:7979/python.html {'Python': 51}\n")

        input_file.close()
        output_file.close()

    def test_2(self):
        input_file = NamedTemporaryFile()
        output_file = NamedTemporaryFile()

        with open(input_file.name, "w", encoding="utf-8") as fout:
            print("http://localhost:5555/wiki.html", file=fout)

        client_fout = open(output_file.name, "w", encoding="utf-8")

        file_server = subprocess.Popen(
            ["python3", "-m", "http.server", "-d", "tests/", "5555"]
        )

        server = subprocess.Popen(
            ["python3", "server.py", "-w", "1", "-k", "1", "-p", "9000"]
        )

        sleep(1)

        client = subprocess.Popen(
            ["python3", "client.py", "1", input_file.name, "-p", "9000"],
            stdout=client_fout,
        )

        client.wait()
        server.kill()
        file_server.kill()

        server.wait()
        file_server.wait()

        client_fout.close()

        with open(output_file.name, "r", encoding="utf-8") as fin:
            result = fin.read()

        self.assertEqual(result, "http://localhost:5555/wiki.html {'the': 46}\n")

        input_file.close()
        output_file.close()


if __name__ == "__main__":
    unittest.main()
