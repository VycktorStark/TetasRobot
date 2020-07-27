import lang, os, random
LN = os.environ['LN']
TR = lang.languages
SECRET_KEY = os.environ['SECRET_KEY']
IDBOT =  SECRET_KEY[:9]
TELEGRAM_API = f'https://api.telegram.org/bot{SECRET_KEY}'
FIX = [{
	'nsfw': random.choice(['boobs','butts']),
	'butts': 'butts', 
	'bundas': "butts",
	'bunda': "butts",
	'culos': "butts",
	'boobs': 'boobs', 
	'tetas': "boobs",
	'teta': "boobs",
	'ajuda': "help",
	'help': 'help', 
	'start': 'help', 
	'sobre': "about",
	'about': 'about',
	'ping': 'ping',
	}]
