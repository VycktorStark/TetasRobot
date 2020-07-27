from main import flask, json, requests, msg_receive_, app, cfg

def replace_command(text):
	text = text.replace('/','').lower().split()[0]
	subsss = cfg['FIX']
	for i in subsss[0]:
		if text == i:
			return subsss[0][i]

@app.errorhandler(404)
def server_error(e):
	return flask.Response(status=200)

@app.before_request
def handler():
	if (flask.request.method == 'GET') and (flask.request.path == "/start"):
		params = dict(url = "{}/webhook".format(flask.request.host), max_connections = int(1), allowed_updates = "message")
		r = requests.get(f"{cfg['TELEGRAM_API']}/setWebhook",params=params).json() 
		return flask.Response(response=r['description'], status=200)
	
	elif (flask.request.method == 'POST') and (flask.request.path == "/webhook"):
		msg = flask.request.get_json(silent=True, force=True)
		if ('message' in msg):
			msg = msg['message']
			if ("language_code" in  msg['from']):
				cfg['LN'] = msg['from']['language_code'][:2]
			if ('text' in msg) and ("entities" in msg):
				if ("bot_command" in msg['entities'][0]['type']):
					cmd = replace_command(msg['text'])
					if (cmd):
						return msg_receive_(msg, cmd, cfg['LN'])
			else:
				return flask.Response(status=200)
