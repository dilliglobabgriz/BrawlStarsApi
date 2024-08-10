from ApiRequest import Api_Request
from typing import List

def getUserInput():
    player_tag = input('Player Tag: #')
    brawler = input('Brawler: ')
    info = input('Stat: ')
    a = Api_Request()
    a.set_player_tag(player_tag)
    brawler_info = a.get_brawler_info(brawler)
    print(brawler_info.get(info))

def account_progress(player_id: str='GGGL8900') -> str:
    a = Api_Request()
    a.set_player_tag(player_id)
    gadget_ratio: str = f'{a.get_total_gadgets()}/{a.get_max_gadgets()}'
    sp_ratio: str = f'{a.get_total_star_powers()}/{a.get_max_star_powers()}' 
    gears: str = f'{a.get_total_gears()}'
    progress_message: str = f'Gadgets: {gadget_ratio}\nStar Powers: {sp_ratio}\nGears: {gears}'
    return progress_message

def all_brawlers() -> None:
    a = Api_Request()
    print(len(a.get_general_brawler_info()))


def isaac_vs_grant():
    print("--- Isaac's account progress ---")
    print(account_progress())
    print(f"\n--- Grants's account progress ---")
    print(account_progress('99GL8LLY'))
    #getUserInput()
    
def top_10_info():
    a = Api_Request()
    top_ten_tags: List[str] = a.get_leaderboard_player_tags()
    player_names: List[str] = []
    for tag in top_ten_tags:
        a.set_player_tag(tag[1:])
        player_names.append(a.get_gamer_tag())
    return player_names


def main():
    print(top_10_info())

if __name__ == '__main__':
    main()
