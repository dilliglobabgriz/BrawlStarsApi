from package.ApiRequest import Api_Request

# This player tag is from a non active accout, information about it should not change
def test_get_total_gears():
    a = Api_Request()
    a.set_player_tag('2GV90R0V')
    total_gears = a.get_total_gears()
    assert total_gears == 1