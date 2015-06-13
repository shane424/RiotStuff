URL = {
    'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
    'static': 'https://{proxy}.api.pvp.net/api/lol/static-data/{region}/{url}',
    'observer': 'https://{proxy}.api.pvp.net/{url}',
    'summoner_by_name': 'v{version}/summoner/by-name/{names}',
    'match_history': 'v{version}/matchhistory/{ids}',
    'current_game': 'observer-mode/rest/consumer/getSpectatorGameInfo/{platformId}/{summonerId}',
    'champion_by_id': 'v{version}/champion/{ids}'
}

API_VERSIONS = {
    'summoner': '1.4',
    'matchhist': '2.2',
    'cur_game': '1.0',
    'static_data': '1.2'
}

REGIONS = {
    'europe_nordic_and_east': 'eune',
    'europe_west': 'euw',
    'north_america': 'na'
}
