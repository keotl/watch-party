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
    def __init__(self, timestamp: int):
        super().__init__("PAUSE")
        self.timestamp = timestamp

class PlayMessage(Message):
    def __init__(self, timestamp: int):
        super().__init__("PLAY")
        self.timestamp = timestamp

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

    except:
        pass

    raise MalformedMessageException()
