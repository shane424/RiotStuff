from BalancerAPI import RiotAPI
import BalancerRanks as bb
import time
import pKey as pKey
api = RiotAPI(pKey.api_key)

def getNames():
	names = [None] * 10
	for i in range(10):
		names[i] = raw_input('Enter a summoner name: ')
	print names
	return names

def addTeams():
	#names = getNames()
	names = ['shriuken154',
		  'astrixa',
		  'finley',
		   'finley',
		   'jedithor',
		   'mugyou2',
		   'snorelacks',
		   'physio',
		   'mdragon14',
		   'yourmomse',
		   'kathliks']

	points = bb.divisionPoints
	theStuff = {}
	for name, val in enumerate(names):
		idd = api.get_summoner_by_name(names[name])
		theId = idd[val]['id']
		mm = str(theId)
		try:
			tier = api.get_league_entry(theId)[mm][0]['tier']
			div = api.get_league_entry(theId)[mm][0]['entries'][0]['division']
		except ValueError:
			tier = 'UNRANKED'
			div = ''
		theStuff[val] = tier + div
		time.sleep(4)
	#print theStuff
	return theStuff

def getCount():
	names = addTeams()
	points = bb.divisionPoints
	moreStuff = {}
	for name in enumerate(names):
		for i in points:
			if names[name[1]] == i:
				moreStuff[name[1]] = points[i]

	return moreStuff
	
def organizeTeam():
	names = getCount()
	newStuff = {}
	for name in enumerate(names):
		#print names[name[1]]
		for i in enumerate(names):
			if names[name[1]] < names[i[1]] and names[name[1]] is not names[i[1]]:
				tmp = names[name[1]]
				names[name[1]] = names[i[1]]
				names[i[1]] = tmp
	#print names
	return names

def makeTeam():
	names = organizeTeam()
	team1 = {}
	team2 = {}
	count = 0
	tcount1 = 0
	tcount2 = 0
	for name, val in enumerate(names):
		if count == 2 or count == 5 or count == 6 or count == 0 or count == 9:
			team1[tcount1] = val
			tcount1 += 1
		elif count == 1 or count == 3 or count == 4 or count == 7 or count == 8:
			team2[tcount2] = val
			tcount2 += 1
		count += 1
	return team1, team2

def main():
	#api = RiotAPI('69dd6296-fc43-4b5e-905c-65aaaa4cca12')
	#r = api.get_summoner_by_name("mugyou2") # r for response
	#print r['mugyou2']['id'] # r is a dictionary, can do stuff with given ID
							 # can retrieve match history with ID

	#iid = r['mugyou2']['id']
	#mm = str(iid)
	#tier = api.get_league_entry(iid)[mm][0]['tier']
	#div = api.get_league_entry(iid)[mm][0]['entries'][0]['division']
	#print tier + div
	new = makeTeam()
	print new
	#nn = getNames()

if __name__ == "__main__":
	main()