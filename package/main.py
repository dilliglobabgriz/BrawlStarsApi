from ApiRequest import Api_Request

def main():
    a = Api_Request()
    a.set_player_tag('GGGL8900')
    shelly_info = a.get_brawler_info('mortis')
    print(shelly_info.get('power'))

if __name__ == '__main__':
    main()
