#www.youtube.com/watch?v=0NycEiHOeX8
import requests
import RiotConsts as Consts

class RiotAPI(object):
    def __init__(self, api_key, region=Consts.REGIONS['north_america']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}): # regular URL calls
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(      # format allows replacement of strings
                proxy = self.region,
                region = self.region,
                url = api_url
                ), 
            params = args
            )
        #print response.url
        return response.json()
    
    def __request(self, api_url, params={}):   # current game calls
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['observer'].format(      # format allows replacement of strings
                proxy = self.region,
                region = self.region,
                url = api_url
                ), 
            params = args
            )
        #print response.url
        return response.json()

    def ___request(self, api_url, params={}):   # static information calls
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['static'].format(      # format allows replacement of strings
                proxy = self.region,
                region = self.region,
                url = api_url
                ), 
            params = args
            )
        #print response.url
        return response.json()


    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
            proxy = self.region,
            region = self.region,
            version = Consts.API_VERSIONS['summoner'],
            names = name)
        return self._request(api_url)

    def get_match_history(self, summ_id):
        api_url = Consts.URL['match_history'].format(
            region =  self.region,
            version = Consts.API_VERSIONS['matchhist'],
            ids = summ_id)
        return self._request(api_url)

    def get_current_game(self, platId, summ_id):
        api_url = Consts.URL['current_game'].format(
            region = self.region,
            platformId = platId,
            summonerId = summ_id)
        return self.__request(api_url)

    def get_champion_name(self, champ_id):
        api_url = Consts.URL['champion_by_id'].format(
            region = self.region,
            version = Consts.API_VERSIONS['static_data'],
            ids = champ_id)
        return self.___request(api_url)