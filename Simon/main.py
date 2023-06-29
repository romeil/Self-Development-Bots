import discord, os
from chat_bot import ChatBot
from dotenv import load_dotenv
from keep_alive import keep_alive


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def main():
    @client.event
    async def on_ready():
        print("We have logged in as {0.user}".format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        msg = message.content

        if msg.startswith("$simon"):
            async with message.channel.typing():
                await message.channel.send(ChatBot(msg))
        
    keep_alive()
    load_dotenv("discord_key.env")
    client.run(os.getenv("TOKEN"))


if __name__ == "__main__":
    main()