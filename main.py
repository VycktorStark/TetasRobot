import flask, os, sys, json, requests, random
app = flask.Flask('NSFW')
app.config.from_object('settings')
cfg = app.config

def replace_command(text):
	try:
		text = text.replace('/','').split()[0]
		for i in cfg['FIX'][0]:
			if text.lower() == i:
				return cfg['FIX'][0][i]
	except Exception:
		pass
		
@app.errorhandler(404)
def server_error(e):
	return flask.Response(status=200)

@app.before_request
def handler():
	vetor = flask.request.get_json(silent=True, force=True)
	if (flask.request.method == 'GET') and (flask.request.path == "/start"):
		params = dict(url = "{}/webhook".format(flask.request.host), max_connections = int(1), allowed_updates = "message")
		r = requests.get(f"{cfg['TELEGRAM_API']}/setWebhook",params=params).json() 
		return flask.Response(response=r['description'], status=200)
	
	elif (flask.request.method == 'POST') and (flask.request.path == "/webhook"):
		if ('message' in vetor):
			msg, LN = vetor['message'], cfg['LN']
			if ("language_code" in  msg['from']):
				LN = msg['from']['language_code'][:2]
			if ('text' in msg) and ("entities" in msg):
				if ("bot_command" in msg['entities'][0]['type']):
					cmd  = replace_command(msg['text'])
					if not (cmd) is None:
						params = dict(method ='sendMessage', text = cfg['TR'][LN][0]['cmderror'], chat_id = msg['chat']['id'], reply_to_message_id  = msg['message_id'], parse_mode =  "HTML")
						if ('help' in cmd): 
							params['text'] = cfg['TR'][LN][0]['start']
						elif ('about' in cmd):
							params['text'] = cfg['TR'][LN][0]['about']
						elif ('ping' in cmd): 
							params['text'] = 'pong'
						elif ('boobs' in cmd):
							params['method'] = 'sendPhoto'
							url = requests.get('http://api.oboobs.ru/noise/1'.format(cmd))
							params['photo'] = f'http://media.oboobs.ru/{url.json()[0]["preview"]}'
							params['caption'] = "By: @TetasRobot"
						elif ('butts' in cmd):
							url = requests.get(f'http://api.obutts.ru/butts/{random.randint(0,999)}')
							params['photo'] = f'http://media.obutts.ru/{url.json()[0]["preview"]}'
							params['caption'] = "By: @TetasRobot"
						return flask.Response(response=json.dumps(params), headers={'Content-Type':'application/json'},status=200)
			else:
				return flask.Response(status=200)


if __name__ == '__main__':
	app.run(debug=True, port=int(os.getenv('PORT', 3000)), host='0.0.0.0')
