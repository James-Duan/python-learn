import os
import configparser
import unittest


proDir = os.path.split(os.path.realpath(__file__))[0]
config_path = os.path.join(proDir, "config.ini")


class ReadConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_host(self, name):
        host = self.config.get("host", name)
        return host


if __name__ == "__main__":
    print ReadConfig().get_host("pw_api_host")
