import argparse
from xmlrpc.client import ServerProxy


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', choices=['pow', 'add', 'mul', 'div'])
    parser.add_argument('first_number', type=float)
    parser.add_argument('second_number', type=float)
    args = parser.parse_args()

    server = ServerProxy('http://localhost:8000')
    print(getattr(server, args.operation)(args.first_number, args.second_number))


if __name__ == '__main__':
    main()
