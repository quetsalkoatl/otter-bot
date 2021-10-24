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
        'https://c.tenor.com/cKK0e-SsvJQAAAAC/baby-otter-walrus.gif',
        'https://c.tenor.com/u26WgBEeNAYAAAAC/otter-belly.gif',
        'https://c.tenor.com/yQoWMMW1uLAAAAAC/otter-otters.gif',
        'https://c.tenor.com/EAch1-Fo_o4AAAAM/sea-otter.gif',
        'https://c.tenor.com/spuQWl7xuKAAAAAM/otter-eating-salad-%D0%B2%D1%8B%D0%B4%D1%80%D0%B0.gif',
        'https://c.tenor.com/dBg-utCpYi0AAAAM/otter-cat.gif',
        'https://c.tenor.com/AV2JwtXcUJwAAAAM/otter-roll-otter.gif',
        'https://c.tenor.com/750REFSTyWkAAAAC/otters-sea.gif',
        'https://c.tenor.com/zao2byCy-ZQAAAAd/hanna-otter.gif',
        'https://c.tenor.com/_r0XOi3cyYsAAAAC/ottern-sucktea.gif',
        'https://c.tenor.com/TXNjBACtFyUAAAAM/otter-spin-otter-play.gif',
        'https://c.tenor.com/XhKhN5nQxFgAAAAM/sakthi-otter.gif',
        'https://c.tenor.com/LI6NWAXF_RoAAAAC/pfsf1968-otter.gif',
        'https://c.tenor.com/1G3ha3W56EwAAAAM/otter-sakthi.gif',
        'https://c.tenor.com/8djzFtDG_J0AAAAC/otter-slam-dunk.gif',
        'https://c.tenor.com/oszRqKDCW6cAAAAM/otter-cute.gif',
        'https://c.tenor.com/GV93UFvN98MAAAAC/clapping-otter.gif',
        'https://c.tenor.com/VRYGG3dt3CsAAAAM/sucktea-otter.gif',
        'https://c.tenor.com/jhY3tyYIFcQAAAAM/biting-smartphone-otter.gif',
        'https://c.tenor.com/bgPaizT7YVQAAAAd/otter-cute.gif',
        'https://c.tenor.com/4GmyiIELWcMAAAAM/otter-kitty.gif',
        'https://c.tenor.com/7BjQG3JtOYMAAAAM/otter-otters.gif',
        'https://c.tenor.com/WqgpWEgjuXwAAAAM/%D0%B2%D1%8B%D0%B4%D1%80%D0%B0-%D0%B5%D1%81%D1%82.gif',
        'https://c.tenor.com/o48DqnL42T4AAAAM/otter-sleep.gif',
        'https://c.tenor.com/2tFguakqSbkAAAAM/funny-animals-good-morning.gif',
        'https://c.tenor.com/wq2aBEsmoesAAAAC/otter-otterly.gif',
        'https://c.tenor.com/G_cJy4aSLfsAAAAd/shook-otter.gif',
        'https://c.tenor.com/LLmLgVVQoE8AAAAC/otter-love-hold-hand.gif',
        'https://c.tenor.com/Fiw6K-qWN9UAAAAd/otter.gif',
        'https://c.tenor.com/EKlPRdcuoccAAAAC/otter-cute.gif',
        'https://gifimage.net/wp-content/uploads/2017/06/otter-gif-5.gif',
        'https://media4.giphy.com/media/26vUGO8U52XTg6vfO/giphy.gif'
    ]

    EXCLUDE_LIST = [
        'mother'
    ]

    EXCLUDE_CHANNELS = [
        'bts-kpop'
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
            await self.send_embed('Sorry to correct you', response, message, random.choice(self.OTTER_LIST))
            return

        if 'otter' in l_msg.replace(' ', ''):
            matches = re.findall(r'o *t *t *e *r', l_msg, flags=re.IGNORECASE)
            for match in matches:
                if len(match) > 5:
                    response = re.sub(r'(\w*)(o *t *t *e *r)(\w*)', r'\1**\2**\3', message.content, flags=re.IGNORECASE)
                    await self.send_embed('Wooo! You found me!', response, message, random.choice(self.OTTER_LIST))
                    return

    async def commands(self, content, message):
        if 'info' in content:
            await self.info(message)
        else:
            await self.info(message)

    async def info(self, message):
        embed = self.embed('Hello', f"Hello. I'm the otter bot {self.OTTER_DANCE}")
        await message.channel.send(embed=embed, reference=message)

    async def send_embed(self, title, description, message, image_url=None):
        for ch in self.EXCLUDE_CHANNELS:
            if ch in message.channel.name:
                return
        embed = self.embed(title, description, image_url)
        await message.add_reaction(self.OTTER_EMOJI)
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
