import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
from typing import Dict, List, Any

class Api_Request:
    def __init__(self):
        self.method = 'get'
        self.BASE_URL = 'https://api.brawlstars.com/v1/'
        load_dotenv()
        self.API_KEY = os.getenv('BS_API_KEY')
        self.player_tag = ''
        self.endpoint = f'players/%23{self.player_tag}'

        self.headers = {
          'Authorization': f'Bearer {self.API_KEY}',
           'Accept': 'application/json'
        }

    # Returns a JSON object
    def get_player_info(self) -> Dict[str, Any]:
        endpoint = self.get_player_info_endpoint()
        response = requests.get(self.BASE_URL + endpoint, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
    
            return data
        else:
            raise Exception(f"Failed to retrieve data: {response.status_code}\n{response.text}")
        
    def get_all_brawlers_info(self) -> List[Dict[str, Any]]:
        player_data = self.get_player_info()
        return player_data.get('brawlers', [])
    
    def get_brawler_info(self, brawler_name: str) -> Dict[str, Any]:
        brawlers = self.get_all_brawlers_info()
        for brawler in brawlers:
            if brawler.get('name') == brawler_name.upper():
                return brawler
            
        raise Exception(f"Could not find {brawler_name}")

    
    def get_player_info_endpoint(self) -> str:
        return f'players/%23{self.player_tag}'
    
    def set_endpoint(self, endpoint):
        self.endpoint = endpoint
        
    def set_player_tag(self, tag):
        self.player_tag = tag
        self.set_endpoint(tag)
    
    def get_player_tag(self) -> str:
        return self.player_tag