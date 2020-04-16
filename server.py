import sys
from xmlrpc.server import SimpleXMLRPCServer


def main():
    with SimpleXMLRPCServer(('localhost', 8000)) as server:
        server.register_function(pow)
        server.register_function(lambda x, y: x + y, 'add')
        server.register_function(lambda x, y: x * y, 'mul')
        server.register_function(lambda x, y: x / y, 'div')
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting.")
            sys.exit(0)


if __name__ == '__main__':
    main()
