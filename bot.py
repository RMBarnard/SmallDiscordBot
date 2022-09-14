import os
from secrets import choice
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands
from duel import battle

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
# client = discord.Client(intents = intents)
TOKEN = os.getenv('DISCORD_TOKEN')


@bot.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message) and message.content.lower().split()[1] == "choose:":
        choice_list = message.content.split()
        choice_list = choice_list[2:]
        await message.channel.send(f"My choice is {random.choice(choice_list)}")


    if "dark" in message.content.lower():
        await message.channel.send('The dark is my home.')

    if "herobrine" in message.content.lower():
        await message.channel.send("Did someone say my name?")

    if "sus" in message.content.lower():
        await message.channel.send("Something is sussy? What's the sus? :eyes: :eyes:")
    await bot.process_commands(message)

@bot.command(name = 'duel')
async def _duel(ctx):
    if bot.user.mentioned_in(ctx.message):
        embed = battle(ctx.message.author.display_name, "Herobrine")
        await ctx.send(embed = embed)
    else:
        await ctx.send(embed = discord.Embed(description="Only Herobrine can be battled at this time"))

@bot.command(name = '8ball')
async def _8ball(ctx):
    responses = ['As I see it, yes.',
                      'Yes.',
                      'Positive',
                      'It is decidely so',
                      'From my point of view, yes',
                      'Convinced.',
                      'Most Likely.',
                      'Chances High',
                      'No.',
                      'Chances low',
                      'Negative.',
                      'Perhaps.',
                      'Not Sure',
                      'Maybe',
                      'I am too tired for silly questions. *proceeds with sleeping*']
    response = random.choice(responses)
    embed = discord.Embed(title="Herobrine's Decision", description=f'Answer: {response}')
    await ctx.send(embed=embed)

bot.run(TOKEN)