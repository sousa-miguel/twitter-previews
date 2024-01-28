import os
import logging
import validators
from dotenv import load_dotenv
from discord import Intents, Client, Message
import responses

# Setup logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()
DISCORD_TOKEN = "DISCORD_TOKEN"
TOKEN = os.getenv(DISCORD_TOKEN)

# Setup BOT
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)


# Setup messages
async def send_message(message: Message, user_message: str) -> None:
    """Sends a message if the user message is a valid Twitter URL and not a vxTwitter URL."""
    if not validators.url(user_message):
        return
    if not responses.validate_twitter_url(user_message):
        return
    if responses.validate_vxtwitter_url(user_message):
        return
    try:
        response: str = responses.get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        logging.error(e)


# Handling bot startup
@client.event
async def on_ready() -> None:
    """Logs a message when the bot has connected to Discord."""
    logging.info(f"{client.user} has connected to Discord!")


# Handling messages
@client.event
async def on_message(message: Message) -> None:
    """Handles incoming messages."""
    if message.author == client.user:  # Prevent bot from responding to itself
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    logging.info(f'{username} sent "{user_message}" in {channel}')
    await send_message(message, user_message)


# Run bot
def main() -> None:
    """Runs the bot."""
    client.run(TOKEN)


if __name__ == "__main__":
    main()
