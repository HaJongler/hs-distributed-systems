import argparse
from datetime import datetime
from threading import Thread
from xmlrpc.client import ServerProxy
from time import sleep


class MsgFetcher(Thread):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.server = ServerProxy('http://localhost:8000')

    def run(self):
        last_fetch = datetime.now()
        while self.server.check_user_active(self.user):
            try:
                msgs = self.server.get_messages(last_fetch)
                for msg in msgs:
                    print(msg)
            except:
                pass
            last_fetch = datetime.now()
            sleep(0.1)



class ChatClient(object):

    def __init__(self, user_name):
        self.user = user_name
        self.server = ServerProxy('http://localhost:8000')
        self.server.start_session(self.user)

    def chat(self):

        while True:
            msg = input()
            if msg.strip() == '':
                continue

            elif msg == '/quit':
                self.server.end_session(self.user)
                print('Bye bye!')
                break

            elif msg == '/list':
                print(self.server.list_users())
                continue

            elif msg.startswith('/kick'):
                to_kick = msg.split()[1]
                self.server.kick_user(to_kick)
                continue

            else:
                self.server.add_message(self.user, msg)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('user_name')
    args = parser.parse_args()

    print(f'Welcome {args.user_name}')
    client = ChatClient(args.user_name)
    fetcher = MsgFetcher(args.user_name)
    fetcher.start()
    client.chat()


if __name__ == '__main__':
    main()
