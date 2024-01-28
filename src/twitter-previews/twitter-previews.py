import os
from typing import Final
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response, validate_twitter_url
import validators

# Load environment variables
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Setup BOT
intents: Final[Intents] = Intents.default()
intents.message_content = True
client: Final[Client] = Client(intents=intents)

# Setup messages
async def send_message(message: Message, user_message: str) -> None:
    if not validators.url(user_message):
        return
    if not validate_twitter_url(user_message):
        return
    try:
        response: str = get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

# Handling bot startup
@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!')

# Handling messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user: # Prevent bot from responding to itself
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'{username} sent "{user_message}" in {channel}')
    await send_message(message, user_message)

# Run bot
def main() -> None:
    client.run(TOKEN)

if __name__ == '__main__':
    main()