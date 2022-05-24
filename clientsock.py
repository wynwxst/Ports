#!/usr/bin/env python

import asyncio
import websockets

async def hello():
    uri = "ws://127.0.0.1:8182"
    async with websockets.connect(uri) as websocket:


        await websocket.send("event:connect ello\nkey:default")


        greeting = await websocket.recv()
        print(greeting)


if __name__ == "__main__":
    asyncio.run(hello())
