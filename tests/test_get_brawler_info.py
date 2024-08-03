from package.ApiRequest import Api_Request

def test_get_brawler_info_id():
    a = Api_Request()
    a.set_player_tag('GGGL8900')
    brawler_info = a.get_brawler_info('cOlT')

    assert brawler_info.get('id') == 16000001

def test_get_brawler_info_power():
    a = Api_Request()
    a.set_player_tag('GGGL8900')
    brawler_info = a.get_brawler_info('barley')

    assert brawler_info.get('power') == 6
