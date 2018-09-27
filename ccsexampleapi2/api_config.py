import os

ENV_API_BASE_URL = "CCS_API_BASE_URL"
ENV_API_PROTOCOL = "CCS_API_PROTOCOL"
ENV_APP_BASE_URL = "CCS_APP_BASE_URL"
ENV_APP_PROTOCOL = "CCS_APP_PROTOCOL"
ENV_FEATURE_PREFIX = "CCS_FEATURE_"

class ApiConfig(object):

    @staticmethod
    def instance():
        return _apiConfig

    #
    # Protocol used for Application URLs
    #
    _app_protocol = "http"

    #
    # Base application URL
    #
    _app_base_url = "roweitdev.co.uk"

    #
    # Protocol used for API URLs
    #
    _api_protocol = "http"

    #
    # Base API URL
    #
    _api_base_url = "ccsdev-internal.org"

    #
    # Map of boolean flags indicating what features are enabled
    #
    _feature_info = {}

    #
    # Private constructor to create the config object
    #
    def __init__(self):
        # Read what we can from the environment
        for k, v in os.environ.items():
            ev_test = k.upper().strip()
            if ev_test == ENV_API_BASE_URL:
                _api_base_url = v.strip()
            elif ev_test == ENV_API_PROTOCOL:
                _api_protocol = v.strip()
            elif ev_test == ENV_APP_BASE_URL:
                _app_base_url = v.strip()
            elif ev_test == ENV_APP_PROTOCOL:
                _app_protocol = v.strip()
            elif ev_test.startswith(ENV_FEATURE_PREFIX):
                # Determine if the feature is enabled
                feature_name = ev_test[len(ENV_FEATURE_PREFIX):]
                val = v.upper().strip()
                enabled = val in ['ON', 'ENABLED', 'TRUE', 'YES']
                self._feature_info[feature_name] = enabled

    #
    # Obtains a complete path to the specified API
    #
    # @param apiName
    # @return API URL
    #
    def api_url( self, api_name ):
        return self._api_protocol + "://" + api_name + "." + self._api_base_url

    #
    # Called to determine if a particular feature is enabled.
    #
    # @param featureName
    # @return true if the feature is enabled
    #
    def is_feature_enabled( self, feature_name ):

        enabled = False

        if feature_name in self._feature_info:
            enabled = self._feature_info[feature_name]

        return enabled

    #
    # @return Protocol used for Application URLs
    #
    def app_protocol( self ):
        return self._app_protocol

    #
    # @return Base URL for application URLs
    #
    def app_base_url( self ):
        return self._app_base_url

    #
    # @return Protocol used for API URLs
    #
    def api_protocol( self ):
        return self._api_protocol

    #
    # @return Base URL for API URLs
    #
    def api_base_url( self ):
        return self._api_base_url


_apiConfig = ApiConfig()
