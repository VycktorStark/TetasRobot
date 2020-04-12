* * *
                  _   _      ____   _____   __        __
                 | \ | |   /  __|  |  ___|  \ \      / /
                 |  \| |   \__ \   | |_      \ \ /\ / / 
                 | |\  |   __)  |  |  _|      \ V  V /  
                 |_| \_|  |____/   |_|         \_/\_/   

* * *

## Getting Started

These instructions will provide you with a copy of the project and show you how to get started using it for development and testing purposes.

## Configuring the bot to run on the terminal
You must have your machine up to date and have Python 3 installed, as well as some modules, such as: flask and requests, and if you don't have it, you'll need to install it this way here:
```
# Tested on Ubuntu 14.04, 15.04 and 16.04, Debian 7, Linux Mint 17.2
$ sudo apt-get update && sudo apt-get upgrade   
$ sudo apt install python3 && python3-pip
$ sudo pip3 install flask && requests
```
With everything installed, we will now clone the repository like this:

```
$ git clone https://github.com/VycktorStark/nsfw.git
```

Now, with the repository installed, you should observe your bot's settings via [BotFather](http://telegram.me/BotFather), if you don't have one you need to create (more information on the [Bots official FAQ page](https://core.telegram.org/bots/faq#what-messages-will-my-bot-get))

> Make sure privacy is turned off. Send `/setprivacy` to [BotFather](http://telegram.me/BotFather), to check the current configuration.

After performing the check, with a text editor, make the following changes to the "settings.py" file:
> •   Defines the language of the bot in "LN", which should only contain two characters. (example: LN = "en")

> •   Also define your bot's token in "SECRET_KEY", (example: SECRET_KEY = "12345669: JHIhdsjEOJoEIOjoih7hjih")

## Boot process

- To start the bot, run: sudo ./run.py
- To stop the bot, press Ctrl + D.
You can also start the bot with python3 run.py

Note: the project is via webhook, that is, you need a way to receive the request, I guide ngrok provisionally (soon I will put a function to switch between webhook and polling)

## Configuring the bot to run on heroku

Click the button below and configure your language, also setting your bot's token.

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

ready, now go to: https://projectname.com.br/start

Note: replace "project name" with the name of your project

Only this will make your project start working normally
