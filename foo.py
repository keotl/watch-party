import asyncio
import websockets
import json

from time import time
from typing import Any, Dict


async def hello():
    # uri = "wss://continuum-rt.app.pxel.pw/community/my-community"
    uri = "ws://localhost:8080/ws"
    # uri = "/tmp/rt.sock"
    async with websockets.connect(uri) as websocket:
        while True:
            message_to_send = input()
            if message_to_send.replace(" ", "") != "":
                await websocket.send(message_to_send)

            print(await websocket.recv())


asyncio.get_event_loop().run_until_complete(hello())
