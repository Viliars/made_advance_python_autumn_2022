import argparse
from server_workers.master import Master


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--workers", type=int, help="Workers count")
    parser.add_argument(
        "-k", "--ktop", type=int, help="The number of most frequent words"
    )
    parser.add_argument(
        "-p", "--port", type=int, default=8000, help="Server port"
    )

    args = parser.parse_args()

    server = Master(args.workers, args.ktop, args.port)

    server.start_server()


if __name__ == "__main__":
    main()
