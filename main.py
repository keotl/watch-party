from watch_party.communication.message_receiver import MessageReceiver
from jivago.jivago_application import JivagoApplication
import watch_party
import asyncio
import websockets
from websockets.exceptions import ConnectionClosedError

app = JivagoApplication(watch_party)


async def main(websocket, path):
    receiver = app.serviceLocator.get(MessageReceiver)
    name = await receiver.add_user(path, websocket)
    try:
        async for message in websocket:
            await receiver.receive_message(path, message, name)
        # await websocket.send(message)
    except ConnectionClosedError:
        print(f"Closed connection for {name}.")
        receiver.remove_user(path, name)

if __name__ == '__main__':

    # start_server = websockets.serve(main, "0.0.0.0", "8080")
    start_server = websockets.unix_serve(main, "/tmp/rt.sock")

    loop = asyncio.get_event_loop()
    # loop.create_task(message_receiver.listen(loop))
    loop.run_until_complete(start_server)

    loop.run_forever()
