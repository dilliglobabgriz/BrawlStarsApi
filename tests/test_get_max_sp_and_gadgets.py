from package.ApiRequest import Api_Request
import pytest

def test_get_max_star_powers():
    a = Api_Request()
    a.set_player_tag('2GV90R0V')
    total_sps = a.get_max_star_powers()

    assert total_sps == a.get_total_brawlers() * 2

def test_get_max_gadgets():
    a = Api_Request()
    a.set_player_tag('2GV90R0V')
    total_gadgets = a.get_max_gadgets()

    assert total_gadgets == a.get_total_brawlers() * 2