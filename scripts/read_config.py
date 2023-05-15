import json


def read_conf(url: str = "./config/options.conf", mode="r", encoding="UTF8") -> dict:

    try:
        file = open(url)
        config = json.loads(file.read())
        file.close()
        return config
    except:
        return None

