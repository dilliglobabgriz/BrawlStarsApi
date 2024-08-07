import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
from typing import Dict, List, Any

class Api_Request:
    def __init__(self):
        self.method: str = 'get'
        self.BASE_URL: str = 'https://api.brawlstars.com/v1/'
        load_dotenv()
        self.API_KEY: str = os.getenv('BS_API_KEY')
        self.player_tag: str = ''
        self.endpoint: str = f'players/%23{self.player_tag}'

        self.headers: Dict[str, str] = {
          'Authorization': f'Bearer {self.API_KEY}',
           'Accept': 'application/json'
        }

    # Returns a JSON object
    def get_player_info(self) -> Dict[str, Any]:
        endpoint: str = self.get_player_info_endpoint()
        response = requests.get(self.BASE_URL + endpoint, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
    
            return data
        else:
            raise Exception(f"Failed to retrieve data: {response.status_code}\n{response.text}")
        
    def get_all_brawlers_info(self) -> List[Dict[str, Any]]:
        player_data: Dict[str, Any] = self.get_player_info()
        return player_data.get('brawlers', [])
    
    def get_brawler_info(self, brawler_name: str) -> Dict[str, Any]:
        brawlers: List[Dict[str, Any]] = self.get_all_brawlers_info()
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
    
    def get_total_gears(self) -> int:
        gear_sum: int = 0
        brawlers: List[Dict[str, Any]] = self.get_all_brawlers_info()
        for brawler in brawlers:
            gear_sum += len(brawler.get('gears'))
        return gear_sum
    
    def get_total_star_powers(self) -> int:
        star_power_sum: int = 0
        brawlers: List[Dict[str, Any]] = self.get_all_brawlers_info()
        for brawler in brawlers:
            star_power_sum += len(brawler.get('starPowers'))
        return star_power_sum
    
    def get_total_gadgets(self) -> int:
        gadget_sum: int = 0
        brawlers: List[Dict[str, Any]] = self.get_all_brawlers_info()
        for brawler in brawlers:
            gadget_sum += len(brawler.get('gadgets'))
        return gadget_sum
        
