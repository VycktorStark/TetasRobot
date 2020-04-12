from main import flask, os, json, requests, msg_receive_, app, cfg

def replace_(text):
	subsss = cfg['FIX']
	for i in subsss[0]:
		if text == i:
			return subsss[0][i]

@app.errorhandler(404)
def server_error(e):
	return flask.Response(status=200)

@app.before_request
def handler():
	if (flask.request.method == 'GET') and (flask.request.path == "/webhook_int"):
		params = dict(url = "{}/webhook".format(flask.request.host), max_connections = int(1), allowed_updates = "message")
		url = "{}{}".format(cfg['TELEGRAM_API'], 'setWebhook')
		r = requests.get(url,params=params).json() 
		return flask.Response(response=r['description'], status=200)
	
	elif (flask.request.method == 'POST') and (flask.request.path == "/webhook"):
		msg = flask.request.get_json(silent=True, force=True)['message']
		if ("language_code" in  msg['from']) is True:
			cfg['LN'] = msg['from']['language_code'][:2]
		if ('text' in msg) and ("entities" in msg) is True:
				if ("bot_command" in msg['entities'][0]['type']) is True:
					cmd = msg['text'].replace('/','').lower().split()
					cmd = replace_(cmd[0])
					return msg_receive_(msg, cmd, cfg['LN'])
		else:
			return flask.Response(status=200)
