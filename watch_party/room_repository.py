import threading
from typing import Dict
from watch_party.room import Room
from jivago.inject.annotation import Component, Singleton

@Component
@Singleton
class RoomRepository(object):

    def __init__(self):
        self._rooms: Dict[str, Room] = {}
        self._lock = threading.Lock()

    def get_room(self, room_id: str) -> Room:
        with self._lock:
            if not room_id in self._rooms:
                self._rooms[room_id] = Room()

            return self._rooms[room_id]
