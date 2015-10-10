#www.youtube.com/watch?v=0NycEiHOeX8
import requests
import RiotConsts as Consts

class RiotAPI(object):
    def __init__(self, api_key, region=Consts.REGIONS['north_america']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
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
        print response.url
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
            proxy = self.region,
            region = self.region,
            version = Consts.API_VERSIONS['summoner'],
            names = name)
        return self._request(api_url)

    def get_ranked_stats(self, summ_id):
        api_url = Consts.URL['summoner_ranked'].format(
            region = self.region,
            version = Consts.API_VERSIONS['stats'],
            summonerId = summ_id)
        return self._request(api_url)

    def get_league_entry(self, summ_id):
        api_url = Consts.URL['leagues'].format(
            region = self.region,
            version = Consts.API_VERSIONS['league'],
            summonerIds = summ_id)
        return self._request(api_url)
