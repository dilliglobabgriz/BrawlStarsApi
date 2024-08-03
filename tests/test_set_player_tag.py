from package.ApiRequest import Api_Request

def test_set_player_tag():
    a = Api_Request()
    a.set_player_tag('GGGL8900')

    assert a.get_player_tag() == 'GGGL8900'

def test_set_player_tag_endpoint_check():
    a = Api_Request()
    a.set_player_tag('GGGL8900')

    assert a.get_player_info_endpoint() == f'players/%23GGGL8900'

def test_set_player_tag_fullURL():
    a = Api_Request()
    a.set_player_tag('GGGL8900')

    fullUrl = f'{a.BASE_URL}{a.get_player_info_endpoint()}'
    assert fullUrl == f'https://api.brawlstars.com/v1/players/%23GGGL8900'
