from BalancerAPI import RiotAPI
import BalancerRanks as bb
api = RiotAPI('69dd6296-fc43-4b5e-905c-65aaaa4cca12')

def getNames():
	for i in range(1):
		names = [raw_input('Enter a summoner name: ')]
	#print type(names[0])
	return names

def balanceTeams():
	names = getNames()
	theStuff = []
	for name, val in enumerate(names):
		idd = api.get_summoner_by_name(names[name])
		theId = idd[val]['id']
		mm = str(theId)
		tier = api.get_league_entry(theId)[mm][0]['tier']
		div = api.get_league_entry(theId)[mm][0]['entries'][0]['division']
		print tier + div

def main():
	#api = RiotAPI('69dd6296-fc43-4b5e-905c-65aaaa4cca12')
	r = api.get_summoner_by_name("mugyou2") # r for response
	print r['mugyou2']['id'] # r is a dictionary, can do stuff with given ID
							 # can retrieve match history with ID

	#iid = r['mugyou2']['id']
	#mm = str(iid)
	#tier = api.get_league_entry(iid)[mm][0]['tier']
	#div = api.get_league_entry(iid)[mm][0]['entries'][0]['division']
	#print tier + div
	new = balanceTeams()
	#nn = getNames()

if __name__ == "__main__":
	main()