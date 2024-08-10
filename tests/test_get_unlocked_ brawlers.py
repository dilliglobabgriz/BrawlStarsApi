from package.ApiRequest import Api_Request

def test_get_unlocked_brawlers():
    a = Api_Request()
    a.set_player_tag('2GV90R0V')
    num_brawlers = a.get_unlocked_brawlers()

    assert num_brawlers == 33