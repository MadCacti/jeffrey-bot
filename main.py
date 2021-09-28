import discord 
import random 
from discord.ext import commands 

intents = discord.Intents().all()
intents.members = True
client = commands.Bot(command_prefix = '~', intents = intents)

@client.command()
async def flipacoin(ctx):
    headsortails = ['Heads!', 'Tails!', 'Heads?', 'Tails?', 'Heads?!', 'Tails!?', 'Heads.', 'Tails.']
    await ctx.send(f'{random.choice(headsortails)}')

@client.command()
async def pingjeffrey(ctx):
    await ctx.message.delete()
    await ctx.send(f"<@{userid}>") 
    
@client.command()
async def percent(ctx):
    percentage = (random.randint(0, 100))
    await ctx.send(f'{percentage}%')

@client.event
async def on_member_update(before, after):
    guild = client.get_guild(guildid)
    role = discord.utils.get(before.guild.roles, name="rolename") # make sure user has role
    if after in role.members:
        if after.status is discord.Status.offline:
            channel = client.get_channel(channelid)
            await channel.send('(name) is dead! Wake up 'f"<@{userid}>!")  
        if after.status is discord.Status.do_not_disturb:
            channel = client.get_channel(channelid)
            await channel.send('(name) is alive! RUN FOR THE HILLS!')
        if after.status is discord.Status.online:
            channel = client.get_channel(channelid)
            await channel.send('(name) is alive! RUN FOR THE HILLS!!! SAVE YOURSELVES')
            
@client.command()   # This one's optional, it's just rhotacism
async def jeffrey(ctx, *, string):
    await ctx.message.delete()
    string = string.replace("r", "w")
    string = string.replace("l", "w")
    string = string.replace("R", "W")
    string = string.replace("L", "W")
    await ctx.send(f'{string}')

client.run('token')
