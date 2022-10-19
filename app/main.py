import keyCheck
import dsCommon


def main():
    print(f"ds-docker init")

    try:
        trend_host, trend_api_key = keyCheck.init()
    except False:
        print(f"Keyfile not found, quitting.")
        quit()

    try:
        api_config = dsCommon.trend_api_configuration(trend_host, trend_api_key)
        api_config = api_config.get_configuration()
    except:
        print(f"Trend API configuration not able to be set.")
        quit()

    try:
        keyCheck.describe_key(api_config)
    except:
        print(f"Key could not be described.")
        quit()


if __name__ == "__main__":
    main()
