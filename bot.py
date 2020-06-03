import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="-")


@bot.event
async def on_ready():
	print("Online")
	await bot.change_presence(activity=discord.Game(name='watching shaik asif'))
print("made by shaikasif")


@bot.event
async def on_member_join(member):
        print(f'{member} has joined server.')

@bot.event 
async def on_member_remove(member):
        print(f'{member} has left server.')
@bot.command()
async def Hi(ctx):
      await ctx.send(f'Hello!')
@bot.command()
async def hq(ctx):
        await ctx.send(f'Fetching HQ answers, please wait!')
@bot.command()
async def qp(ctx):
       await ctx.send(f'Fetching Quipp answers!')
       

bot.run("NzE3MjU0ODA5NjIyNjc1NDk5.XtYLCg.oPAQcMvcV2fMIgSgcII2IqKHPls")
