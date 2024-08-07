from package.ApiRequest import Api_Request

# This player tag is from a non active accout, information about it should not change
def test_get_total_star_powers():
    a = Api_Request()
    a.set_player_tag('2GV90R0V')
    total_star_powers = a.get_total_star_powers()
    assert total_star_powers == 4