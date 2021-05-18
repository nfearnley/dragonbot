from pathlib import Path

import appdirs
import toml


def getDataDir():
    appname = "DragonBot"
    appauthor = "D&N"
    datadir = Path(appdirs.user_data_dir(appname, appauthor))
    return datadir


prefix = "!"
authtoken = None

# File paths
datadir = getDataDir()
confpath = datadir / "dragonbot.conf"


def load():
    global prefix, authtoken
    configDict = toml.load(confpath)
    prefix = configDict.get("dragonbot", {}).get("prefix", prefix)
    authtoken = configDict.get("discord", {}).get("authtoken", authtoken)
