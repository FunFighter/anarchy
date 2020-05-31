import discord
from discord.ext import commands
import random
import time

async def editer(ctx,role):
    '''
    Build a bear is a user defined role that has edit perssions that are non admin
    nothing below buildABear role should have any admin.
    This grants the user a set time to edit the server
    '''

    member = ctx.message.author
    print(f'{member} has turned on build a bear')
    role = discord.utils.get(ctx.guild.roles, name = "Build a Bear") 
    await member.add_roles(role)
    time.sleep(60)
    await member.remove_roles(role)
    print(f'{member} is no longer a build a bear')
    
    
async def blackList(ctx):
    '''
    This needs to be revisted
    ban the whole other list if the other users joins.
    '''
    mems = ctx.guild.members
    badBoys = ['replops#0141','brenny#5149','Rudy#1000','xXxDemonDemonxXx#5043']

    for bad in badBoys:
        if (str(ctx) in badBoys):
            for mem in mems:
                if (str(mem) == bad):
                    print(f'{mem}   {type(mem)}\n')
                    await mem.ban(reason='BlackListed')
    return


async def banList(ctx):
    banned_users = await ctx.guild.bans()
    '''
    Loops over and sends the currrent ban list back to the user.
    '''
    for ban_entry in banned_users:
        user = ban_entry.user
        print(user.name)
        await ctx.send(f'{user.name}#{user.discriminator}\n')
        
async def freedom(ctx, *, member,command_name):
    '''
     is unban user wil look for a selected user's name in the banlist and unban from there.
    '''
    banned_users = await ctx.guild.bans()
    try:
        member_name, member_discriminator = member.split('#')
        print('before loop')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                print(f'{user.name} in unbansection ')
                await ctx.guild.unban(user)
                await ctx.send(f'https://tenor.com/view/baby-come-back-gif-9673680')
            else: 
                print('here')
                pass
            
    except Exception as e:
        print(f'{e}')
        print('there')
        await ctx.send(f'{str(member)} is not in the band list. Check banlist with .banList')
        print('I want this to ignore cooldown')
        #this is so that if the user isn't in the list the cooldown is not triggered.
        command_name.reset_cooldown(ctx)

async def ban(ctx,  member, *, reason=None,command_name):
    '''
    This will ban a user after a time. 
    '''
    print(f'{member}')
    print(f'{ctx.message.author} has tried to kick {member}')
    await ctx.send(f'{member} you have 20 seconds before termination.\n https://tenor.com/view/simon-cowell-look-stare-red-eyes-laser-gif-12692635')
    time.sleep(20)
    await member.ban(reason="murdered")

async def kicker(ctx, member, *, reason=None,command_name):
    ''' This will insta kick a user, .kick @user'''
    print(f'{ctx.message.author} has tried to kick {member}')
    if isinstance(member,discord.member.Member):
        print('member was a member class')
        await member.kick(reason='Murdered')
    else:
        print('memeber was not of the member calss')
        command_name.reset_cooldown(ctx)
        await ctx.send(f'mem was {type(member)}')

async def rr(ctx,*,message):
    '''
    Russian Roulette takes an int from 1-6
    with a 1/6 chance to get banned if they numbers match.
    '''
    try:  
        msg = int(message)
        if (msg >= 1) and (msg <= 6):  
            await ctx.send('Russian Roulette protocol initialized')   
            # set bullet to random int 1-6
            bullet = random.randint(1,6)
            time.sleep(3)
            if (bullet == msg):
                await ctx.send(f'https://tenor.com/view/elmo-fire-gif-5042503')
                await ctx.send(f'I will never forget you.')
                
                time.sleep(7)
                await ctx.message.author.ban(reason='Russian Roulette')
                
            else:
                await ctx.send(f'https://www.youtube.com/watch?v=QslJYDX3o8s')
                await ctx.send(f'You live this time SpongeBob')
            
        else:
            await ctx.send(f'"{message}" is not a vaild whole number. Please select a number between 1 and 6.')
        
    except:
        await ctx.send(f'"{message}" is not a vaild whole number. Please select a number between 1 and 6.')
