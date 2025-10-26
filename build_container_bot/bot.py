# https://qiita.com/PitaQ/items/832eee4d7bc79d92ff31
# https://pypi.org/project/mcrcon/
from mcrcon import MCRcon
import os

# アドレス、パスワード、ポートの定義
ADDRESS = os.getenv('minecraft_server_config_rcon_host', 'localhost')
PASSWORD = os.getenv('minecraft_server_config_rcon_password', '')
PORT = os.getenv('minecraft_server_config_rcon_port', 25575)

def main(address, password, port):
  with MCRcon(address, password, port) as rcon:
    # コマンドを送信する
    rcon.command("list")

if __name__ == '__main__':
  main(ADDRESS, PASSWORD, PORT)
