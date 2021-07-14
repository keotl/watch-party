from watch_party.communication.channel import WebsocketChannel
from watch_party.inbound_messages import parse_message
from watch_party.room_repository import RoomRepository
from jivago.inject.annotation import Component
from jivago.lang.annotations import Inject
import json
from uuid import uuid4

@Component
class MessageReceiver(object):

    @Inject
    def __init__(self, room_repository: RoomRepository):
        self._room_repository = room_repository

    async def add_user(self, room_id: str, websocket) -> str:
        try:
            room = self._room_repository.get_room(room_id)
            id = str(uuid4())
            await room.add_user(WebsocketChannel(websocket, id))
            return id
        except:
            pass
        return ""
        
    async def receive_message(self, room_id: str, message: str):
        try:
            parsed = parse_message(json.loads(message))
            room = self._room_repository.get_room(room_id)
            await room.receive_message(parsed)
        except:
            pass

    def remove_user(self, room_id: str, name: str):
        try:
            if name == "":
                return
            room = self._room_repository.get_room(room_id)
            room.remove_user(name)
        except:
            pass
