from typing import List
from watch_party.inbound_messages import Message, PauseMessage, PlayMessage, SetUrlMessage
from watch_party.communication.channel import Channel
import threading
from jivago.lang.stream import Stream

class RoomState(object):

    def __init__(self, url: str, is_playing: bool, timestamp: int):
        self._url = url
        self._is_playing = is_playing
        self._timestamp = timestamp
        

class Room(object):

    def __init__(self) -> None:
        self._channels: List[Channel] = []
        self._lock = threading.Lock()
        self._state = RoomState("", False, 0)

    async def add_user(self, user_channel: Channel):
        with self._lock:
            self._channels.append(user_channel)
            await self._notify_channel(user_channel)
    
    async def receive_message(self, message: Message):
        with self._lock:
            if isinstance(message, SetUrlMessage):
                self._state._url = message.url
                self._state._timestamp = 0
            elif isinstance(message, PlayMessage):
                self._state._is_playing = True
                self._state._timestamp = message.timestamp
            elif isinstance(message, PauseMessage):
                self._state._is_playing = False
                self._state._timestamp = message.timestamp

            for c in self._channels:
                await self._notify_channel(c)


    async def _notify_channel(self, channel: Channel):
        await channel.send(SetUrlMessage(self._state._url))
        if self._state._is_playing:
            await channel.send(PlayMessage(self._state._timestamp))
        else:
            await channel.send(PauseMessage(self._state._timestamp))

    def remove_user(self, name: str):
        with self._lock:
            self._channels = Stream(self._channels).filter(lambda c: c.name() != name).toList()
        
