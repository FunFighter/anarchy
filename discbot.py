import discord
from discord.ext import commands
import random
import time
import requests
import mods
from apikey import APIKEY

from discord.ext.commands import CommandNotFound

client = commands.Bot(command_prefix = '.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error
 
@client.event
async def on_ready():
    print('Anarchy Initiated')
    
@client.command()
@commands.cooldown(1, 10800, commands.BucketType.user)
async def kick(ctx, member : discord.Member, *, reason=None):
    await mods.kicker(ctx = ctx,member = member, reason=None,command_name=kick)

@client.command()
@commands.cooldown(1, 10800, commands.BucketType.user)
async def murder(ctx, member : discord.Member, *, reason=None):
    await mods.ban(ctx = ctx, member = member, reason=None,command_name=murder)

@client.command()
@commands.cooldown(1, 4, commands.BucketType.user)
async def rr(ctx, *,message= ''):
    await mods.rr(ctx=ctx,message=message)

@client.command(cooldown_after_parsing=True)
@commands.cooldown(1, 10800, commands.BucketType.user)
async def unban(ctx, *, member):
    await mods.freedom(ctx = ctx, member = member,command_name = unban)
    
@client.command()
async def banList(ctx):
    await mods.banList(ctx = ctx)

@client.event
async def on_member_remove(ctx):
    print(f'{ctx} has been executed')

@client.event
async def on_member_join(ctx):
    print(f'{ctx} has joined')
    await mods.blackList(ctx)
    
#does pass context even need to be there???
@client.command(pass_context = True)
@commands.cooldown(1, 1800, commands.BucketType.user)
async def buildABear(ctx):
    await mods.editer(ctx,role ='Build a Bear')
    
client.run(APIKEY)
