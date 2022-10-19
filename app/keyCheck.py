import re
import urllib3
import deepsecurity as ds
from deepsecurity.rest import ApiException


def describe_key(api_config):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    api_key_api = ds.APIKeysApi(ds.ApiClient(api_config))
    api_version = "v1"

    try:
        api_response = api_key_api.describe_current_api_key(api_version)
        print(api_response)
    except ApiException:
        print(ApiException)


def init():
    try:
        keyfile = open("/ds-docker/config/keyfile.config")
    except:
        print(f"keyfile.config could not be opened, quitting.")
        return False
    else:
        keyfile = keyfile.read()
        trend_host = re.search("(?<=trend_host=).*", keyfile).group().strip()
        trend_api_key = re.search("(?<=trend_api_key=).*", keyfile).group().strip()
        return trend_host, trend_api_key
