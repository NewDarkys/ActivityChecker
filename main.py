import http.client
import json
import time
import os
import discord
from discord.ext.commands import Bot


TOKEN = os.getenv('TOKEN')
PLACE_ID = os.getenv('PLACE_ID')

bot = discord.Bot("!rhstn", intents=discord.Intents.all())
prevCCU = 0
@bot.event
async def on_ready():
    global prevCCU
    print(f'{bot.user} has connected to Discord!')
    bot_channel = bot.get_channel(1236070147685486794)
    while True:
        conn = http.client.HTTPSConnection('games.roblox.com')
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'origin': 'https://www.roblox.com',
            'referer': 'https://www.roblox.com/',
            'sec-ch-ua': '"Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0 (Edition Yx 08)',
        }
        conn.request('GET', '/v1/games?universeIds='+int(PLACE_ID), headers=headers)
        response = conn.getresponse()
        if response.status == 200:
            online = json.loads(response.read().decode("utf-8"))['data'][0]["playing"]
            if online != prevCCU:
                prevCCU = online
                await bot_channel.edit(name = "Онлайн-"+str(online), topic = 'Suck')
        conn.close()
        time.sleep(10)
    
bot.run(str(TOKEN))
