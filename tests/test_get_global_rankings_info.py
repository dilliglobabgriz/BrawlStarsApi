from package.ApiRequest import Api_Request

def test_get_global_rankings_info_default_param_check():
    a = Api_Request()
    top_ten = a.get_global_rankings_info()

    assert len(top_ten) == 10

def test_get_global_rankings_info_param_check():
    a = Api_Request()
    top_100 = a.get_global_rankings_info(100)

    assert len(top_100) == 100





