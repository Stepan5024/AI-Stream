import os

from dotenv import load_dotenv
from loggingmixin import LoggingMixin
from twitchio.ext import commands


class Bot(commands.Bot, LoggingMixin):

    async def event_ready(self):
        self.logger.info(f'Bot {self.nick} is ready!')

    async def event_message(self, message):
        if message.author.name.lower() == self.nick.lower():
            return

        # TODO: check user in cache
        # TODO: check message in cache

        self.logger.info(f'{message.author.name}: {message.content}')

        # Example
        if 'DELETE' in message.content.upper():
            try:
                await message.delete()
                self.logger.info(f'Message {message.content} from {message.author.name} has been deleted.')
            except Exception as e:
                self.logger.info(f"Can't delete a message {message.content}. Got exception: {e}")

        await self.handle_commands(message)


if __name__ == "__main__":
    load_dotenv()

    bot = Bot(
        token=os.environ["TWITCH_API_TOKEN"],
        prefix="!",
        initial_channels=os.environ["TWITCH_INITIAL_CHANNELS"].split(",")
    )
    bot.run()
