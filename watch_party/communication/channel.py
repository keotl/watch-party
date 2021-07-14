from abc import abstractmethod, ABC

from jivago.lang.annotations import Override
from watch_party.inbound_messages import Message

class Channel(ABC):

    @abstractmethod
    async def send(self, message: Message):
        raise NotImplementedError

    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

class WebsocketChannel(Channel):

    def __init__(self, websocket, name: str):
        self._websocket = websocket
        self._name = name
    
    @Override
    async def send(self, message: Message):
        await self._websocket.send(message)

    @Override
    def name(self) -> str:
        return self._name
