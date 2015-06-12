from RiotAPI import RiotAPI

def main():
	api = RiotAPI('cc003a0a-41af-4433-a047-2b0d1f9474e9')
	r = api.get_summoner_by_name("mugyou2") # r for response
	print r['mugyou2']['id'] # r is a dictionary, can do stuff with given ID
							 # can retrieve match history with ID
if __name__ == "__main__":
	main()