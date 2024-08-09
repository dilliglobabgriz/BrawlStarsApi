from package.ApiRequest import Api_Request

def test_get_total_trophies():
    a = Api_Request()
    a.set_player_tag('2GV90R0V')
    trophies = a.get_total_trophies()

    assert trophies == 12006