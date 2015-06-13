from APItest import RiotAPI

def main():
	api = RiotAPI('17e0b6ed-59fd-4b61-903c-53ff5c5824c5')
	#r = api.get_summoner_by_name("mugyou2") # r for response
	r = api.get_summoner_by_name("corndog911")
	#rr = api.get_match_history('19832192') # <- physio id
	#rr = api.get_match_history('503892')
	#print r['mugyou2']['id'] # r is a dictionary, can do stuff with given ID
							 # can retrieve match history with
	#print rr['matches']['season']
	#print rr['matches'][2]['matchType'] #returns match_type
	#print rr['matches'][1]['participantIdentities'][0]['player']   # [int] picks which game. up to 10, (0-9)
	#print r['mugyou2']
	#print r['corndog911']['id']		# prints summoners ID
	#g = api.get_current_game('NA1','503892')
	g = api.get_current_game('NA1','38290145')
	count = 0
	for i in g['participants']:			# prints all 10 players in game
		#print g['participants'][i]['summonerName']
		name = g['participants'][count]['summonerName']	# Prints the ith summoner name
		print g['participants'][count]['summonerName']
		#print g['participants'][count]['championId']
		#print g['participants'][count]['teamId']
		print api.get_champion_name(g['participants'][count]['championId'])['name']
		count += 1
		print " "

if __name__ == "__main__":
	main()