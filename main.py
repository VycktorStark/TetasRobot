import flask, os, sys, json, requests
app = flask.Flask('NSFW')
app.config.from_object('settings')
cfg = app.config

def msg_receive_(msg, cmd, ln):
	params = dict(
			method ='sendMessage',
			text = cfg['TR'][ln][0]['cmderror'],
			chat_id = msg['chat']['id'],
			reply_to_message_id  = msg['message_id'],
			parse_mode =  "HTML"
			)
	print(cmd)
	if ('help' in cmd) is True: 
		params['text'] = cfg['TR'][ln][0]['start']
	elif ('about' in cmd) is True:
		params['text'] = cfg['TR'][ln][0]['about']
	elif ('ping' in cmd) is True: 
		params['text'] = 'pong'
	elif ('boobs' in cmd) or ('butts' in cmd) or ('nsfw' in cmd):
		params['method'] = 'sendPhoto'
		url = requests.get('http://api.o{}.ru/noise/1'.format(cmd))
		params['photo'] = 'http://media.o{}.ru/{}'.format(cmd, url.json()[0]["preview"])
		params['caption'] = "By: @TetasRobot"
	return flask.Response(response=json.dumps(params), headers={'Content-Type':'application/json'},status=200)

import handler
