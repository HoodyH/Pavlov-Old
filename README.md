# Pavlov Bot
- On telegram search "BotFather" (official telegram bot creator), start and type /newbot then follow the instructions.
- Create on the root of the project a file /configs/pavlov.cfg with the following structure
```bash
[creds]
TOKEN = your_bot_token

[admins]
OWNER_ID = 12345678  # the owner id of the bot
LOGGING_CHAT = 12345678  # the id of the chat where send logs

[debug]
DEBUG = true  # there is a debug if you want to use it
```

## How to install
#### On Ubuntu/Debian
```bash
$ pip install -r requirements.txt
$ sudo apt install ffmpeg
```
#### On Windows
```bash
$ pip install -r requirements.txt
```
Now install ffmpeg:
- download a build of ffmpeg https://ffmpeg.zeranoe.com/builds/
- unzip it and put the content in **C:\ffmpeg**
- add it to system path (from admin CMD): **setx /M PATH "C:\ffmpeg\bin;%PATH%"**

## How to run
```bash
$ python3 server.py
```

## Commands
The commands are divided in modules.
Use .man command_name to see the manual
#### Management:
- help -- help message
- man -- command manual of all active commands
- data -- get user stats
- stt -- speech to text
#### Stats:
- level -- show your level
- ranking -- show ranking of the top 10

