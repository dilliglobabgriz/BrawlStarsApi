from ApiRequest import Api_Request

def getUserInput():
    player_tag = input('Player Tag: #')
    brawler = input('Brawler: ')
    info = input('Stat: ')
    a = Api_Request()
    a.set_player_tag(player_tag)
    brawler_info = a.get_brawler_info(brawler)
    print(brawler_info.get(info))

def account_progress() -> str:
    a = Api_Request()
    a.set_player_tag('GGGL8900')
    gadget_ratio: str = f'{a.get_total_gadgets()}/{a.get_max_gadgets}'
    sp_ratio: str = f'{a.get_total_star_powers()}/{a.get_max_star_powers}' 
    progress_message: str = f'Gadgets: {gadget_ratio}\nStar Powers: {sp_ratio}'
    return progress_message

def all_brawlers() -> None:
    a = Api_Request()
    print(len(a.get_general_brawler_info()))


def main():
    #print(account_progress())
    all_brawlers()
    

if __name__ == '__main__':
    main()
