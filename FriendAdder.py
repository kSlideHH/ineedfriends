import threading
import time
from g_python.hunitytools import UnityRoomUsers


class FriendAdder:
    def __init__(self, extension, roomUsers: UnityRoomUsers):
        self.__extension = extension
        self.roomUsers = roomUsers
        self.roomUsers.on_new_users(self.__on_new_users)

        self.__verbose = True

    def __on_new_users(self, users):
        thread = threading.Thread(target=self.__process_users, args=(users,))
        thread.start()

    def __process_users(self, users):
        for user in users:
            self.__extension.send_to_server('{l}{h:39}{s:"' + user.name + '"}')
            self.log(f'Sent friend request to {user}')
            time.sleep(0.05)

    def log(self, message):
        if self.__verbose:
            print(f'({time.strftime("%d %b %Y %H:%M:%S", time.gmtime())}) <INeedFriends> {message}')
