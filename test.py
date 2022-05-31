import json
import requests
import asyncio
from datetime import datetime
import sys
import time
import hashlib
import hmac



# quote asset volume BTC/USDT = USDT volume
# taker buy base asset volume
# taker buy quote asset volume
async def btcusdt():
    # file_path = "test.txt"
    # sys.stdout = open(file_path, "a")
    r = requests.get('https://api.binance.com/api/v3/klines',{'symbol': "BTCUSDT", 'interval': '1m', 'limit': '3'})
    candle_list = json.loads(r.text)
    length_list = len(candle_list)
    i= 0
    nbr_trade = 0
    nbr_validate = 0
    while i < length_list:
        await calcul(candle_list[i])
        await volume(candle_list[i])

        i += 1
    # print("\n"+"\033[1;37m total ",nbr_trade," / valid",nbr_validate, " / invalid",nbr_trade - nbr_validate, ' / date ', datetime.now())
async get_support():

# async def calcul(candle):
#     body_candle = float(candle[1]) - float(candle[4])     # ouverture - fermeture
#     body_with_shadow = float(candle[2]) - float(candle[3])   # plus haut - plus bas
#     if body_candle > 0:                                       # bougie vente
#         shadow_top = float(candle[1]) - float(candle[2])      # ouverture - plus haut 
#         shadow_bot = float(candle[4]) - float(candle[3])      # fermeture - plus bas
#         return {'body': body_candle,'bodyWithShadow':body_with_shadow,'shadowTop': shadow_top,'shadowBot':shadow_bot}
#     else:                                                     # bougie achat
#         shadow_top = float(candle[4]) - float(candle[2])      # fertmeture - plus haut   
#         shadow_bot = float(candle[1]) - float(candle[3])       # ouverture - plus bas
#         return {'body': body_candle,'bodyWithShadow':body_with_shadow,'shadowTop': shadow_top,'shadowBot':shadow_bot}        

# async def volume(candle):
#     print("\033[37m " + str(candle[5]))

# async def testTrade():
#     time.sleep(2)
#     dt= datetime.now()
#     milliseconds = int(round(dt.timestamp()* 1000))
#     msg = 'symbol=BTCUSDT&side=BUY&type=MARKET&quantity=1&timestamp='+str(milliseconds)
#     signature = hmac.new(SECRET_KEY.encode('utf-8'), msg.encode('utf-8'), hashlib.sha256).hexdigest()
#     signature_two =  hmac.new(bytes(SECRET_KEY , 'utf-8'), msg = bytes(msg , 'utf-8'), digestmod = hashlib.sha256).hexdigest()
#     print(signature)
#     print(signature_two)
#     myobj={'symbol':'BTCUSDT','side':'BUY','type':'MARKET','quantity':1,'timestamp' :str(milliseconds), 'signature': signature }
#     r = requests.post('https://api.binance.com/api/v3/order/test',data=myobj ,headers= {'X-MBX-APIKEY': API_KEY, 'Content-type':'application/x-www-form-urlencoded'})
#     print(r.text,' // ',r.status_code)

asyncio.run(btcusdt())
# asyncio.run(testTrade())
