import random
import discord
import os
import re
from dotenv import load_dotenv
from os.path import exists


class OtterClient(discord.Client):
    OTTER_EMOJI = '🦦'
    OTTER_DANCE = '<:OtterDance:892768067652841472>'
    IGNORE_FOOTER = 'If you want me to ignore your messages type `botter ignore me`'
    NOTICE_FOOTER = 'If you want me respond to your messages type `botter notice me`'

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
        'https://media4.giphy.com/media/26vUGO8U52XTg6vfO/giphy.gif',
        'https://c.tenor.com/fy2qB_-pAA8AAAAd/otter-cuddles-cuddles.gif',
        'https://c.tenor.com/AV2JwtXcUJwAAAAd/otter-roll-otter.gif'
    ]

    EXCLUDE_LIST = [
        'mother'
    ]

    EXCLUDE_CHANNELS = [
        651962874956087302,  # welcome
        651962893474070528,  # rules
        651962914739060748,  # announcements
        824285620972945428,  # live-reaction-request
        877731529751683073,  # custom-reactions
        882695801887936572,  # non-music-reaction-suggestions
        661629181913989163   # double-takes
    ]

    EXCLUDE_CATEGORIES = [
        664879021745635333,  # staff
        652609720238211103,  # destiny updates
        663311896304418825   # giveaways
    ]

    EXCLUDE_USERS_FILE = "blacklist.txt"

    EXCLUDE_USERS = set()

    def __init__(self, **options):
        super().__init__(**options)
        self.load_blacklist()

    async def on_message(self, message):
        l_msg = message.content.lower()
        if l_msg.startswith('botter'):
            await self.commands(l_msg[6:].strip(), message)
            return

        if 'other' in l_msg:
            if not self.is_excluded(message):
                return await self.other_response(message, l_msg)

        if 'otter' in l_msg.replace(' ', ''):
            if not self.is_excluded(message):
                return await self.ot_ter_response(message, l_msg)

    async def other_response(self, message, l_msg):
        for ex in self.EXCLUDE_LIST:
            if ex in l_msg:
                return
            # fancy regex substitution to replace 'other' with 'otter' ignoring case
        response = re.sub(r'((\w*)other(\w*))', r'~~\1~~ \2otter\3', message.content, flags=re.IGNORECASE)
        await self.send_embed('Sorry to correct you', response, message, random.choice(self.OTTER_LIST))

    async def ot_ter_response(self, message, l_msg):
        matches = re.findall(r'o *t *t *e *r', l_msg, flags=re.IGNORECASE)
        for match in matches:
            if len(match) > 5:
                response = re.sub(r'(\w*)(o *t *t *e *r)(\w*)', r'\1**\2**\3', message.content, flags=re.IGNORECASE)
                await self.send_embed('Wooo! You found me!', response, message, random.choice(self.OTTER_LIST))

    async def commands(self, content, message):
        if content in ["enable", "on", "notice", "notice me"]:
            await self.remove_blacklist(message)
        elif content in ["disable", "off", "ignore", "ignore me"]:
            await self.add_blacklist(message)
        else:
            await self.info(message)

    async def info(self, message):
        status = "notice me"
        if message.author.id in self.EXCLUDE_USERS:
            status = "ignore me"
        embed = self.embed('Hello', f"I'm the otter bot {self.OTTER_DANCE}\n"
                                    f"\n"
                                    f"**Status**: {status}\n"
                                    f"\n"
                                    f"**Commands:\n**"
                                    f"If you find me annoying I'll ignore you with `botter ignore me`.\n"
                                    f"Otterwise I'll respond to you again with `botter notice me`\n"
                                    f"\n"
                                    f"Remember we're all here to have fun.")
        await message.channel.send(embed=embed, reference=message)

    async def remove_blacklist(self, message):
        self.EXCLUDE_USERS.remove(message.author.id)
        self.write_blacklist()
        embed = self.embed('Welcome back',
                           f"I'm glad you're allowing me to respond to your messages again. {self.OTTER_DANCE}",
                           footer=self.IGNORE_FOOTER)
        await message.channel.send(embed=embed, reference=message)

    async def add_blacklist(self, message):
        self.EXCLUDE_USERS.add(message.author.id)
        self.write_blacklist()
        embed = self.embed('Bye', f"I'll ignore you until you decide otterwise. 👋\n", footer=self.NOTICE_FOOTER)
        await message.channel.send(embed=embed, reference=message)

    async def send_embed(self, title, description, message, image_url=None, footer=IGNORE_FOOTER):
        embed = self.embed(title, description, image_url, footer)
        await message.add_reaction(self.OTTER_EMOJI)
        await message.channel.send(embed=embed, reference=message)

    def is_excluded(self, message):
        if message.channel.id in self.EXCLUDE_CHANNELS:
            return True
        category = message.channel.category
        if category is not None and category.id in self.EXCLUDE_CATEGORIES:
            return True
        user_id = message.author.id
        if user_id in self.EXCLUDE_USERS:
            return True
        return False

    def load_blacklist(self):
        if exists(self.EXCLUDE_USERS_FILE):
            with open(self.EXCLUDE_USERS_FILE, "r") as fp:
                for line in fp.readlines():
                    self.EXCLUDE_USERS.add(int(line))

    def write_blacklist(self):
        with open(self.EXCLUDE_USERS_FILE, "w") as fp:
            for value in self.EXCLUDE_USERS:
                fp.write(str(value) + "\n")

    @staticmethod
    def embed(title, description, image_url=None, footer=None):
        embed = discord.Embed(title=title, description=description)
        if image_url is not None:
            embed.set_image(url=image_url)
        if footer is not None:
            embed.set_footer(text=footer)
        return embed


def main():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    client = OtterClient()
    client.run(token)


if __name__ == "__main__":
    main()
