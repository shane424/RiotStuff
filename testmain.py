from APItest import RiotAPI

def main():
    api = RiotAPI('0b46853b-a841-4780-b884-d5a08790aaff')
    #r = api.get_summoner_by_name("mugyou2") # r for response
    r = api.get_summoner_by_name("corndog911")
    #rr = api.get_match_history('19832192') # <- physio id
    #print r['mugyou2']['id'] # r is a dictionary, can do stuff with given ID
    						 # can retrieve match history with
    #print rr['matches']['season']
    #print rr['matches'][2]['matchType'] #returns match_type
    #print rr['matches'][1]['participantIdentities'][0]['player']   # [int] picks which game. up to 10, (0-9)
    #print r['mugyou2']
    #print r['corndog911']['id']		# prints summoners ID
    #g = api.get_current_game('NA1','503892')
    #@@@@
    #@@@@@@@
      # get's summoner names
    '''
    g = api.get_current_game('NA1','31501243')
    names_in_game = {}
    ids_in_game = {}
    count = 0
    for i in g['participants']:			# prints all 10 players in game
    	names_in_game[count] = (g['participants'][count]['summonerName'])		#print g['participants'][i]['summonerName']
    	ids_in_game[count] = (g['participants'][count]['summonerId'])
    	name = g['participants'][count]['summonerName']	# Prints the ith summoner name
    	print g['participants'][count]['summonerName']
    	#print g['participants'][count]['championId']
    	#print g['participants'][count]['teamId']
    	#print api.get_champion_name(g['participants'][count]['championId'])['name']
    	count += 1
    	print " "
    print names_in_game
    #for n in ids_in_game:
    	#stats = api.get_ranked_stats(ids_in_game[n])
    	#print stats#['champions']
     #@@@@@@@@@
    #@@@@@@@@@ End summoner name retrieval
    '''
    #
    #
    '''
    #@@@@@@@@@ Begin Match History Retrieval
    rr = api.get_match_history('31501243')
    print rr['matches'][1]['participants'][0]['participantId']
    champ_id = rr['matches'][9]['participants'][0]['championId'] # retrives champion ID 
    numb_of_kills = rr['matches'][9]['participants'][0]['stats']['kills'] # retrieves last game played kills
    numb_of_assists = rr['matches'][9]['participants'][0]['stats']['assists']
    numb_of_deaths = rr['matches'][9]['participants'][0]['stats']['deaths']
    lane = rr['matches'][9]['participants'][0]['timeline']['lane']
    print champ_id
    champ_name = api.get_champion_name(champ_id)
    print champ_name['name']
    print numb_of_kills
    print numb_of_assists
    print numb_of_deaths
    print lane
    #print champ_name['name']
    league_rank = api.get_league('38290145')
    league_rank2 = api.get_league('503892')
    
    print league_rank['38290145'][0]['tier']#['queue'][1]['RANKED_SOLO_5x5'][0]['tier']
    print league_rank['38290145'][0]['entries'][0]['division']#['entries']['playerOrTeamName' == 'corndog911']['division']
    print league_rank['38290145'][0]['entries'][0]['leaguePoints']
    print league_rank2['503892'][0]['tier']
    print league_rank2['503892'][0]['entries'][0]['division']
    print league_rank2['503892'][0]['entries'][0]['leaguePoints']
    '''
    #@@@@@@@@@@@ End History Retrieval
    
    #@@@@@@@@@@@ Retrieve Champion Ids @@@@@@@@@@@@@@@#
    #champ_names =  api.get_champ_ids()
    c = 0
    champ_ids = {}
    champ_names =  api.test_ids()
    for i in champ_names['champions']:
        print champ_names['champions'][c]['id']
        champ_ids[c] = champ_names['champions'][c]['id']
        c += 1
    #print champ_names['id']
    #print champ_names['data']['Shaco']
    #stck = api.get_static_info()
    #print stck['keys']
    print champ_ids
    #@@@@@@@@@@@@@ End Champion Id Retrieval @@@@@@@@@@@@@@#
    
    #role = api.get_champ_roles('503892')
    #print role['playerRole']



if __name__ == "__main__":
    main()
