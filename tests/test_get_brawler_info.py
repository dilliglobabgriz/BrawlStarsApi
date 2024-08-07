from package.ApiRequest import Api_Request
import pytest

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

def test_get_brawler_info_fake_name():
    with pytest.raises(Exception) as e_info:
        a = Api_Request()
        a.set_player_tag('GGGL8900')
        a.get_brawler_info('barney')

def test_get_brawler_info_fake_tag():
    with pytest.raises(Exception) as e_info:
        a = Api_Request()
        a.set_player_tag('fake')
        a.get_brawler_info('barley')

    
