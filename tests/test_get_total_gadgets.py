from package.ApiRequest import Api_Request

def test_get_total_gadgets():
    a = Api_Request()
    a.set_player_tag('2GV90R0V')
    total_gadgets = a.get_total_gadgets()
    assert total_gadgets == 11