import discord
import asyncio
import random

client = discord.Client()

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
        
    elif message.content.startswith('실험 戊호!'):
        async for log in client.logs_from(message.channel, limit=1):
            if log.author == message.author:
                await client.delete_message(log)
        em = discord.Embed()
        em.set_image(url="https://i.imgur.com/xXk8nVo.gif")
        await client.send_message(message.channel, embed=em)
        
client.run('NDY0NDQzMjc0NDQzMzU4MjA5.Dh_CPg.uCPNZRenyArtUAcCJKR6utMSXhs')
