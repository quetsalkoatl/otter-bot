import random
import discord
import os
import re
from dotenv import load_dotenv


class OtterClient(discord.Client):

    OTTER_EMOJI = '🦦'
    OTTER_DANCE = '<:OtterDance:892768067652841472>'

    # add more links to otter gifs to this list
    OTTER_LIST = [
        'https://media0.giphy.com/media/1xlGfZ07Dq62jqKT9t/giphy.gif',
        'https://media0.giphy.com/media/26gssIytJvy1b1THO/giphy.gif',
        'https://gifimage.net/wp-content/uploads/2017/06/otter-gif-5.gif',
        'https://66.media.tumblr.com/ed029e03114cbe9b96df28b75c344630/tumblr_okunffDlnm1w0433po1_500.gif',
        'https://media0.giphy.com/media/pDt9e4dO0BYWI/giphy.gif',
        'https://media4.giphy.com/media/26vUGO8U52XTg6vfO/giphy.gif'
    ]

    EXCLUDE_LIST = [
        'mother'
    ]

    async def on_message(self, message):
        l_msg = message.content.lower()
        if l_msg.startswith('botter'):
            await self.commands(l_msg[6:].strip(), message)
            return
        if 'other' in l_msg:
            for ex in self.EXCLUDE_LIST:
                if ex in l_msg:
                    return
            # fancy regex substitution to replace 'other' with 'otter' ignoring case
            response = re.sub(r'((\w*)other(\w*))', r'~~\1~~ \2otter\3', message.content, flags=re.IGNORECASE)
            embed = self.embed('Sorry to correct you', response, random.choice(self.OTTER_LIST))
            await message.add_reaction(self.OTTER_EMOJI)
            await message.channel.send(embed=embed, reference=message)

    async def commands(self, content, message):
        if 'info' in content:
            await self.info(message)
        else:
            await self.info(message)

    async def info(self, message):
        embed = self.embed('Hello', f"Hello. I'm the otter bot {self.OTTER_DANCE}")
        await message.channel.send(embed=embed, reference=message)

    @staticmethod
    def embed(title, description, image_url=None):
        embed = discord.Embed(title=title, description=description)
        if image_url is not None:
            embed.set_image(url=image_url)
        return embed


def main():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    client = OtterClient()
    client.run(token)


if __name__ == "__main__":
    main()
