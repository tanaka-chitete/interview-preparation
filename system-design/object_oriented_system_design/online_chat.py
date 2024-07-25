from abc import ABCMeta
from enum import Enum

class RequestStatus(Enum):
    PENDING = 0
    ACCEPTED = 1
    REJECTED = 2

class UserService(object):
    def __init__(self):
        self.user_ids = dict() # key: user ID (string), value: user (User)

    def add_user(self, user_id, user_name, hashed_password): pass
    def remove_user(self, user_id): pass
    def add_friend_request(self, requester_user_id, receiver_user_id): pass
    def approve_friend_request(self, requester_user_id, receiver_user_id): pass
    def reject_friend_request(self, requester_user_id, receiver_user_id): pass

class User(object):
    def __init__(self, user_id, user_name, hashed_password):
        self.user_id = user_id
        self.user_name = user_name
        self.hashed_password = hashed_password

    def message_user(self, friend_id, message): pass
    def message_group(self, group_id, message): pass
    def send_friend_request(self, user_id): pass
    def receive_friend_request(self, user_id): pass
    def approve_friend_request(self, user_id): pass
    def reject_friend_request(self, user_id): pass

class Chat(metaclass=ABCMeta):
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.users = list()
        self.messages = list()

class PrivateChat(Chat):
    def __init__(self, user_a, user_b):
        super(PrivateChat, self).__init__()
        self.users.append(user_a)
        self.users.append(user_b)

class GroupChat(Chat):
    def add_user(self, user): pass
    def remove_user(self, user): pass

class Message(object):
    def __init__(self, message_id, content, timestamp):
        self.message_id = message_id
        self.content = content
        self.timestamp = content

class AddRequest(object):
    def __init__(self, requester_user_id, receiver_user_id, request_status, timestamp):
        self.requester_user_id = requester_user_id
        self.receiver_user_id = receiver_user_id
        self.request_status = request_status
        self.timestamp = timestamp
        