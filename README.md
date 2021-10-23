### Dependencies
```
pip install python-dotenv discord.py
```

### .env

```
DISCORD_TOKEN=xyz
```

### register as linux service
...

### create bot
1. goto https://discord.com/developers/applications
2. create new application
3. (Bot) add new bot
4. (OAuth2) check "bot" scope
5. (OAuth2) check permissions
   - "Send Messages"
   - "Public Threads"
   - "Send Messages in Threads"
   - "Embed Links"
   - "Attach Files"
   - "Add Reactions"
6. copy authorization URL in browser
7. select discord server