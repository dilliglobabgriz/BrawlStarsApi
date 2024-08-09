from package.ApiRequest import Api_Request

def test_get_gamer_tag():
    a = Api_Request()
    a.set_player_tag('GGGL8900')
    tag = a.get_gamer_tag()

    assert tag == 'dilliglobab'