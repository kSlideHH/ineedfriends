import sys

from g_python.gextension import Extension
from g_python.hdirection import Direction

from g_python.hunitytools import UnityRoomUsers

from FriendAdder import FriendAdder

extension_info = {
    "title": "I need friends",
    "description": "adds friends automatically",
    "version": "1.1",
    "author": "kSlide"
}

def on_machine_id(message):
    identifier = message.packet.read_string()
    print(str(identifier))


if __name__ == '__main__':
    extension = Extension(extension_info, sys.argv)
    extension.intercept(Direction.TO_SERVER, on_machine_id, 813)
    extension.start()
    FriendAdder(extension, UnityRoomUsers(extension))
