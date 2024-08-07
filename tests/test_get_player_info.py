from package.ApiRequest import Api_Request
import pytest

def test_get_player_info_fake_id():
    with pytest.raises(Exception) as e_info:
        a = Api_Request()
        a.set_player_tag('fake')
        a.get_player_info()


def test_get_player_info_fake_id2():
    with pytest.raises(Exception) as e_info:
        a = Api_Request()
        a.set_player_tag('#GGGL8900')
        a.get_player_info()
        pytest.fail('If player IDs with preceding # are accepted this should fail')


def test_get_player_info_response_type():
    a = Api_Request()
    a.set_player_tag('GGGL8900')
    info = a.get_player_info()
    assert (type(info) == type({}))
    