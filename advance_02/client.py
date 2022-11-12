import argparse
from client_workers.master import Client


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("workers", type=int, help="Workers count")
    parser.add_argument("filename", type=str, help="File with urls")
    parser.add_argument(
        "-p", "--port", type=int, default=8000, help="Server port"
    )

    args = parser.parse_args()

    client = Client(args.workers, args.filename, args.port)

    client.start_client()


if __name__ == "__main__":
    main()
