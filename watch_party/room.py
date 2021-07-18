from typing import List
from watch_party.inbound_messages import Message, PauseMessage, PlayMessage, SetUrlMessage, RequestResyncMessage
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
            success = await self._request_resync(user_channel.name())
            if not success:
                await self._notify_channel(user_channel)

    async def receive_message(self, message: Message, sender: str):
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
            elif isinstance(message, RequestResyncMessage):
                await self._request_resync(sender)
                return

            to_remove = []
            for i, c in enumerate(self._channels):
                if c.name() == sender:
                    continue
                success = await self._notify_channel(c)
                if not success:
                    to_remove.append(i)
            for i in to_remove[::-1]:
                self._channels.pop(i)

    async def _request_resync(self, sender: str) -> bool:
        for c in self._channels:
            if c.name() == sender:
                continue
            try:
                await c.send(RequestResyncMessage())
                return True
            except:
                continue
        return False

    async def _notify_channel(self, channel: Channel) -> bool:
        ":returns success."
        try:
            await channel.send(SetUrlMessage(self._state._url))
            if self._state._is_playing:
                await channel.send(PlayMessage(self._state._timestamp))
            else:
                await channel.send(PauseMessage(self._state._timestamp))

            return True
        except Exception as e:
            return False

    def remove_user(self, name: str):
        with self._lock:
            self._channels = Stream(self._channels).filter(lambda c: c.name() != name).toList()
