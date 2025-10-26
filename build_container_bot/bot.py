# https://qiita.com/PitaQ/items/832eee4d7bc79d92ff31
# https://pypi.org/project/mcrcon/
from mcrcon import MCRcon
import os
import sys
import time
import traceback
import socket
import json

# アドレス、パスワード、ポートの定義
ADDRESS = os.getenv('minecraft_server_config_rcon_host', 'localhost')
PASSWORD = os.getenv('minecraft_server_config_rcon_password', '')
PORT = os.getenv('minecraft_server_config_rcon_port', 25575)


def loop(interval=0.1):
    # @args interval: [float] unit: second
    while True:
        print(json.dumps({
            "minecraft_server_config_rcon_host": ADDRESS,
            "minecraft_server_config_rcon_password": PASSWORD,
            "minecraft_server_config_rcon_port": PORT,
        }))
        addrs = socket.getaddrinfo(ADDRESS, PORT)
        for addr in addrs:
            print(addr)

        rcon(ADDRESS, PASSWORD, PORT)
        time.sleep(interval)


def rcon(address, password, port):
    with MCRcon(address, password, port) as rcon:
        try:
            # コマンドを送信する
            result = rcon.command("list")
            print(result)
        except (ConnectionRefusedError):
            traceback.format_exc()
            sys.exit(1)


def test_main():
    # pytest
    assert True


if __name__ == '__main__':
    loop(10)
