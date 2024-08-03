from ApiRequest import Api_Request

def main():
    a = Api_Request()
    #a.set_player_tag('failtest')
    print(a.get_brawler_info('shelly'))

if __name__ == '__main__':
    main()
