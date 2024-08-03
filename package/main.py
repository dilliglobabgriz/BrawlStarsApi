from ApiRequest import Api_Request

def getUserInput():
    player_tag = input('Player Tag: #')
    brawler = input('Brawler: ')
    info = input('Stat: ')
    a = Api_Request()
    a.set_player_tag(player_tag)
    brawler_info = a.get_brawler_info(brawler)
    print(brawler_info.get(info))


def main():
    getUserInput()
    '''
    a = Api_Request()
    a.set_player_tag('GGGL8900')
    shelly_info = a.get_brawler_info('mortis')
    print(shelly_info.get('power'))
    '''
    

if __name__ == '__main__':
    main()
