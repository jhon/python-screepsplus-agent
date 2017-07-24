import requests, json, time
import config
import screepsapi

def main():
	api = screepsapi.API(u=config.email,p=config.password,host=config.server_url)
	#print api.memory('stats')
	while True:
		if 'ok' not in api.me() or api.me()['ok']!=1:
			api = screepsapi.API(u=config.email,p=config.password,host=config.server_url)
		
		stats = api.memory('stats')
		if u'data' in stats:
			stats = stats[u'data']

			r = requests.post('https://screepspl.us/api/stats/submit',auth=('token',config.screepsplus_token),json=stats)
			print r.text

		time.sleep(15)

if __name__=="__main__":
	main()
