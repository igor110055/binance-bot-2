import json
import requests
import websockets
import asyncio
from datetime import datetime
import sys

# await websocket.send(json.dumps({"method": "UNSUBSCRIBE","params"``:["shibusdt@kline_1m"],"id": 312})) unsubcribe example

# file_path = "real_time.txt"


async def main():
    # sys.stdout = open(file_path, 'a')
    candle_list = []
    async with websockets.connect("wss://stream.binance.com:9443/ws") as websocket:
        await websocket.send(json.dumps({"method": "SUBSCRIBE", "params": ["btcusdt@kline_1m"], "id": 1}))
        async for message in websocket:
            await getCandle(message, candle_list)


async def getCandle(candle_str, candle_list):
    candle_last = json.loads(candle_str)
    try:
        if candle_last['k']['x']:
            print(candle_last)
            candle_list.append(candle_last)
            if len(candle_list) > 100:
                candle_list.pop(0)
    except KeyError:
        if candle_last['result'] == None:
            print('Connection Reussie')
        pass




    



asyncio.run(main())
