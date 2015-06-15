URL = {
    'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
    'static': 'https://{proxy}.api.pvp.net/api/lol/static-data/{region}/{url}',
    'observer': 'https://{proxy}.api.pvp.net/{url}',
    'summoner_by_name': 'v{version}/summoner/by-name/{names}',
    'match_history': 'v{version}/matchhistory/{ids}',
    'current_game': 'observer-mode/rest/consumer/getSpectatorGameInfo/{platformId}/{summonerId}',
    'champion_by_id': 'v{version}/champion/{ids}',
    'get_champ_id': 'v{version}/champion',
    'summoner_ranked': 'v{version}/stats/by-summoner/{summonerId}/ranked',
    'summoner_summary': 'v{version}/stats/by-summoner/{summonerId}/summary',
    'leagues': 'v{version}/league/by-summoner/{summonerId}/entry',
    'game': 'v{version}/game/by-summoner/{summonerId}/recent',
    'champion_id': 'v{version}/champion'
}

API_VERSIONS = {
    'summoner': '1.4',
    'matchhist': '2.2',
    'cur_game': '1.0',
    'static_data': '1.2',
    'stats': '1.3',
    'league': '2.5'
}

REGIONS = {
    'europe_nordic_and_east': 'eune',
    'europe_west': 'euw',
    'north_america': 'na'
}
