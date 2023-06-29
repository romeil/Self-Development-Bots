import discord, os, datetime, asyncio
from inspire import get_quote
from dotenv import load_dotenv
from keep_alive import keep_alive


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def main():
    @client.event
    async def on_ready():
        print("We have logged in as {0.user}".format(client))
        await daily_quotes()

    async def daily_quotes():
        while True:
            now  = datetime.datetime.now()
            then = now + datetime.timedelta(days=1)
            then.replace(hour=8, minute=30)   
            wait_time = (then-now).total_seconds()
            await asyncio.sleep(wait_time)

            load_dotenv("discord_channel_id.env")
            channel = client.get_channel(os.getenv("ID"))

            await channel.send(get_quote())

    keep_alive()
    load_dotenv("discord_key.env")
    client.run(os.getenv("TOKEN"))

if __name__ == "__main__":
    main()