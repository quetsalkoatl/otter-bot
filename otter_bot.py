import random
import discord
import os
import re
from dotenv import load_dotenv


class OtterClient(discord.Client):
    OTTER_EMOJI = '🦦'

    # add more links to otter gifs to this list
    OTTER_LIST = [
        'https://media0.giphy.com/media/1xlGfZ07Dq62jqKT9t/giphy.gif',
        'https://media0.giphy.com/media/26gssIytJvy1b1THO/giphy.gif',
        'https://gifimage.net/wp-content/uploads/2017/06/otter-gif-5.gif',
        'https://66.media.tumblr.com/ed029e03114cbe9b96df28b75c344630/tumblr_okunffDlnm1w0433po1_500.gif',
        'https://media0.giphy.com/media/pDt9e4dO0BYWI/giphy.gif',
        'https://media4.giphy.com/media/26vUGO8U52XTg6vfO/giphy.gif'
    ]

    async def on_message(self, message):
        # don't reply to own messages
        if message.author == self.user:
            return
        if 'other' in message.content.lower():
            # fancy regex substitution to replace 'other' with 'otter' ignoring case
            response = re.sub(r'((\w*)other(\w*))', r'~~\1~~ \2otter\3', message.content, flags=re.IGNORECASE)
            embed = discord.Embed(title='Sorry to correct you', description=response)
            embed.set_image(url=random.choice(self.OTTER_LIST))
            await message.add_reaction(self.OTTER_EMOJI)
            await message.channel.send(embed=embed, reference=message)


def remove_duplicates(lst):
    return list(dict.fromkeys(lst))


def main():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    client = OtterClient()
    client.run(token)


if __name__ == "__main__":
    main()
