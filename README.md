### Dependencies
```
pip install python-dotenv discord.py pywin32
```

### .env

```
DISCORD_TOKEN=xyz
```

### register as windows service
download nssm (https://nssm.cc/download)
```
nssm install OtterBotService 'C:\Program Files\Python39\python.exe' C:\otter-bot\win_service.py
```
