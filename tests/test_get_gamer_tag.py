import re
from typing import List
from package.ApiRequest import Api_Request

def test_get_gamer_tag():
    a = Api_Request()
    a.set_player_tag('GGGL8900')
    tag = a.get_gamer_tag()

    assert tag == 'dilliglobab'

def test_get_gamer_tags_from_leaderboard():
    a = Api_Request()
    top_ten_tags: List[str] = a.get_leaderboard_player_tags()
    # Convert object into True if it exists
    is_valid_tag = not not re.search("^#[a-zA-Z0-9]+", top_ten_tags[0])

    assert is_valid_tag == True

def test_get_gamer_tags_from_leaderboard2():
    a = Api_Request()
    top_ten_tags: List[str] = a.get_leaderboard_player_tags()
    player_names: List[str] = []
    for tag in top_ten_tags:
        a.set_player_tag(tag[1:])
        player_names.append(a.get_gamer_tag())

    assert len(player_names) == 10
