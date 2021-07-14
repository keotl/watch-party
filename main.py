from jivago.jivago_application import JivagoApplication
import watch_party
import asyncio
import websockets


app = JivagoApplication(watch_party)


async def echo(websocket, path):
    async for message in websocket:
        print(path)
        print(message)
        await websocket.send(message)

if __name__ == '__main__':

    start_server = websockets.unix_serve(echo, "/tmp/rt.sock")

    loop = asyncio.get_event_loop()
    # loop.create_task(message_receiver.listen(loop))
    loop.run_until_complete(start_server)

    loop.run_forever()
