from package.ApiRequest import Api_Request
import pytest

def test_get_leaderboard_player_tags_default():
    a = Api_Request()
    tags = a.get_leaderboard_player_tags()

    assert len(tags) == 10 and type(tags[0]) == str

def test_get_leaderboard_player_tags_me_top_100():
    a = Api_Request()
    top_100 = a.get_leaderboard_player_tags(100)
    is_dilliglobab_top_100 = '#GGGL8900' in top_100

    if is_dilliglobab_top_100:
        pytest.fail('Should only fail if I become a top 100 global player')

    assert is_dilliglobab_top_100 == False
