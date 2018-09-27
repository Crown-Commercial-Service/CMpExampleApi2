from ccsexampleapi2.api_config import ApiConfig

class TestApiConfig(object):

    def test_api_config(self):
        api_config = ApiConfig.instance()
        assert api_config is not None, 'APIConfig factory was None'

    def test_api_url(self):
        api_url = ApiConfig.instance().api_url('api1')
        assert api_url == 'http://api1.ccsdev-internal.org', 'API Url is incorrect'

    def test_is_feature_enabled(self):
        non_existant_feature = ApiConfig.instance().is_feature_enabled('THIS_WONT_EXIST')
        assert non_existant_feature == False, 'No-existant feature'

    def test_app_protocol(self):
        protocol = ApiConfig.instance().app_protocol()
        assert protocol == 'http', 'App protocol should be http'

    def test_app_base_url(self):
        base_url = ApiConfig.instance().app_base_url()
        assert base_url == 'roweitdev.co.uk', 'Base app URL is incorrect'

    def test_api_protocol(self):
        protocol = ApiConfig.instance().api_protocol()
        assert protocol == 'http', 'Api protocol should be http'

    def test_api_base_url(self):
        base_url = ApiConfig.instance().api_base_url()
        assert base_url == 'ccsdev-internal.org', 'Base api URL is incorrect'

