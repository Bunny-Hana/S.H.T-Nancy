import discord
import asyncio
import random

client = discord.Client()
f = open("849728.txt")
f1 = open("158972.txt")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="S.H.T"))

@client.event
async def on_message(message):
    NONSENSE_LIMIT = 999999999999
    if message.content.startswith('Response!'):
        await client.send_message(message.channel, 'Here!')

    elif message.content.startswith('Heya, Nancy!'):
        msg = 'Heya! {0.author.mention}!'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('Response but with delay!'):
        await client.send_message(message.channel, 'Here!')
        msg = await client.wait_for_message(timeout=15.0, author=message.author)

        if msg is None:
            await client.send_message(message.channel, 'Not confirmed!')
            return
        else:
            await client.send_message(message.channel, msg.content)

    elif message.content.startswith('Random Message!'):
        messages = ["Yes!", "Heya!", "Here!"]
        await client.send_message(message.channel, random.choice(messages))
        await asyncio.sleep(120)

    elif message.content.startswith('Delete all!'):
        tmp = await client.send_message(message.channel, 'I will delete all!')
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)

    elif message.content.startswith('Delete me!'):
        async for log in client.logs_from(message.channel, limit=NONSENSE_LIMIT):            
            if log.author == message.author:
                await client.delete_message(log)
  
    elif message.content.startswith('Offline!'):
        await client.logout()

    elif 'S.H.T' in message.content:
        await client.send_message(message.channel, 'Did anyone called me?')
        
    elif message.content.startswith('Exp.1!'):
        async for log in client.logs_from(message.channel, limit=1):
            if log.author == message.author:
                await client.delete_message(log)
        em = discord.Embed()
        em.set_image(url="https://i.imgur.com/xXk8nVo.gif")
        await client.send_message(message.channel, embed=em)
       
    elif message.content.startswith('Delete All!'):
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)

    elif message.content.startswith('Delete Me!'):
        async for log in client.logs_from(message.channel, limit=NONSENSE_LIMIT):
            if log.author == message.author:
                await client.delete_message(log)
                
    elif message.content.startswith('Delete'):
        msg = message.content.split(" ")
        async for log in client.logs_from(message.channel, limit=int(msg[1])): #사용 예시 : Delete 3 3개 메시지만큼을 삭제하라. split 명령어는 " " 내부의 띄어쓰기로 문장을 분리함. int(msg[1])은 띄어쓰기로 나뉜 문장 중 몇번째 구절을 선택할 것인지 표현하는 명령어. 예 : int(msg)[1]은 가 나 다 라 마 바사 중 나 를 고름. [2]는 다 를 고름.
            await client.delete_message(log)
                
    elif message.content.startswith('Delete Command!'):
        async for log in client.logs_from(message.channel, limit=NONSENSE_LIMIT):
            if log.author.id =='464443274443358209':
                await client.delete_message(log)
        
client.run(f.read() + 'A5.DkLC0A.g21IVBgt' + f1.read())
