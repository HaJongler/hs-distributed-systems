from datetime import datetime
from xmlrpc.server import SimpleXMLRPCServer


class ChatServer(object):
    _methods = ['check_user_active', 'add_message', 'start_session', 'get_messages', 'end_session', 'list_users', 'kick_user']

    def __init__(self, address):
        self._users = []
        self._messages = []
        self._server = SimpleXMLRPCServer(address, allow_none=True)
        for method in self._methods:
            self._server.register_function(getattr(self, method))

    def check_user_active(self, user):
        return user in self._users

    def add_message(self, user, message):
        if self.check_user_active(user):
            self._messages.append((datetime.now(), f'{user}: {message}'))
        return True

    def start_session(self, user):
        self._users.append(user)
        print(f'user {user} was added')
        self._messages.append((datetime.now(), f"SERVER: {user} joined the chat!"))
        return True

    def get_messages(self, last_fetch):
        return [msg[1] for msg in self._messages if msg[0] > last_fetch]

    def end_session(self, user):
        self._users.remove(user)
        self._messages.append((datetime.now(), f"SERVER: {user} left the chat!"))
        return True

    def list_users(self):
        return f'Active users: {", ".join(self._users)}'

    def kick_user(self, user):
        if self.check_user_active(user):
            self._users.remove(user)
            self._messages.append((datetime.now(), f"SERVER: {user} was kicked from the chat!"))
        return True


if __name__ == '__main__':
    srv = ChatServer(('', 8000))
    print('Server is running!')
    srv._server.serve_forever()