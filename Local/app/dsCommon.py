import deepsecurity as ds
from deepsecurity.rest import ApiException


class trend_api_configuration:
    def __init__(self, trend_host, trend_api_key, api_version="v1"):
        self.trend_host = trend_host
        self.trend_api_key = trend_api_key
        self.api_version = api_version

    def get_configuration(self):
        configuration = ds.Configuration()
        configuration.host = self.trend_host
        configuration.api_key["api-secret-key"] = self.trend_api_key
        return configuration
