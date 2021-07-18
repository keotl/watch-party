from typing import Optional


class Message(object):
    type: str

    def __init__(self, type: str):
        self.type = type


class SetUrlMessage(Message):
    url: str

    def __init__(self, url: str):
        super().__init__("SET_URL")
        self.url = url


class PauseMessage(Message):
    def __init__(self, timestamp: float):
        super().__init__("PAUSE")
        self.timestamp = timestamp


class PlayMessage(Message):
    def __init__(self, timestamp: float):
        super().__init__("PLAY")
        self.timestamp = timestamp


class RequestResyncMessage(Message):
    def __init__(self):
        super().__init__("REQUEST_RESYNC")


class MalformedMessageException(Exception):
    pass


def parse_message(d: dict) -> Message:
    try:
        if d["type"] == "SET_URL":
            return SetUrlMessage(d["url"])
        if d["type"] == "PAUSE":
            return PauseMessage(d["timestamp"])
        if d["type"] == "PLAY":
            return PlayMessage(d["timestamp"])
        if d["type"] == "REQUEST_RESYNC":
            return RequestResyncMessage()

    except:
        pass

    raise MalformedMessageException()
