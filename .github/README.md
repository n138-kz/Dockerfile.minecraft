# [Dockerfile.minecraft](https://github.com/n138-kz/Dockerfile.minecraft)

## Repos Info

<div align="center">

  [![GitHub repo license](https://img.shields.io/github/license/n138-kz/Dockerfile.minecraft)](/LICENSE)
  [![GitHub top language](https://img.shields.io/github/languages/top/n138-kz/Dockerfile.minecraft)](/../../)
  [![GitHub repo size](https://img.shields.io/github/repo-size/n138-kz/Dockerfile.minecraft)](/../../)
  [![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/n138-kz/Dockerfile.minecraft)](/../../)

</div>
<div align="center">

  [![GitHub last commit](https://img.shields.io/github/last-commit/n138-kz/Dockerfile.minecraft)](/../../commits)
  [![GitHub commit activity](https://img.shields.io/github/commit-activity/w/n138-kz/Dockerfile.minecraft)](/../../commits)
  [![GitHub commit activity](https://img.shields.io/github/commit-activity/t/n138-kz/Dockerfile.minecraft)](/../../commits)
  [![GitHub language count](https://img.shields.io/github/languages/count/n138-kz/Dockerfile.minecraft)](/../../)

</div>
<div align="center">

  [![GitHub issues](https://img.shields.io/github/issues/n138-kz/Dockerfile.minecraft)](/../../issues)
  [![GitHub issues closed](https://img.shields.io/github/issues-closed/n138-kz/Dockerfile.minecraft)](/../../issues)
  [![GitHub pull requests](https://img.shields.io/github/issues-pr/n138-kz/Dockerfile.minecraft)](/../../pulls)
  [![GitHub pull requests closed](https://img.shields.io/github/issues-pr-closed/n138-kz/Dockerfile.minecraft)](/../../pulls)

</div>
<div align="center">

  [![](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/channel/UCOX8Iv1r0V18lbOnohE7lWQ)
  [![](https://img.shields.io/badge/Twitch-6441A5?style=for-the-badge&logo=twitch&logoColor=white)](https://www.twitch.tv/yuukomiya)
  [![](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/n138kz)
  <br>
  [![](https://img.shields.io/youtube/channel/subscribers/UCOX8Iv1r0V18lbOnohE7lWQ)](https://youtube.com/channel/UCOX8Iv1r0V18lbOnohE7lWQ)
  [![](https://img.shields.io/twitch/status/YuuKomiya)](https://www.twitch.tv/yuukomiya)

</div>

## Refs

- [![](https://www.google.com/s2/favicons?size=64&domain=https://github.com)Dockerfile](https://github.com/n138-kz/Dockerfile) [![GitHub last commit](https://img.shields.io/github/last-commit/n138-kz/Dockerfile.minecraft)](https://github.com/n138-kz/Dockerfile)
- [![](https://www.google.com/s2/favicons?size=64&domain=https://github.com)Dockerfile.minecraft](https://github.com/n138-kz/Dockerfile.minecraft) [![GitHub last commit](https://img.shields.io/github/last-commit/n138-kz/Dockerfile.minecraft)](https://github.com/n138-kz/Dockerfile.minecraft)
- [《滅びの呪文》Docker Composeで作ったコンテナ、イメージ、ボリューム、ネットワークを一括完全消去する便利コマンド](https://qiita.com/suin/items/19d65e191b96a0079417)
- [GitHubでQiitaの:::noteみたいな強調をする](https://qiita.com/lobmto/items/d02532134782f34c0e2fs)
- [![](https://www.google.com/s2/favicons?size=64&domain=https://minecraft.net/)Java 版 Minecraft サーバー](https://www.minecraft.net/ja-jp/download/server)
- [Fabric Minecraft Server](https://fabricmc.net/use/server/)
- [![](https://www.google.com/s2/favicons?size=64&domain=https://github.com)Tiiffi/mcrcon](https://github.com/Tiiffi/mcrcon.git)
- [MinecraftのサーバにRCONで接続する | Qiita](https://qiita.com/h_tyokinuhata/items/85d855f88d5d33c21949)

<details>

  <summary>Minecraft Server Each Versions</summary>

  - [![](https://www.google.com/s2/favicons?size=64&domain=https://minecraft.net/)minecraft_server.1.21.1.jar](https://piston-data.mojang.com/v1/objects/59353fb40c36d304f2035d51e7d6e6baa98dc05c/server.jar)
  - [![](https://www.google.com/s2/favicons?size=64&domain=https://minecraft.net/)minecraft_server.1.21.3.jar](https://piston-data.mojang.com/v1/objects/45810d238246d90e811d896f87b14695b7fb6839/server.jar)
  - [![](https://www.google.com/s2/favicons?size=64&domain=https://minecraft.net/)minecraft_server.1.21.8.jar](https://piston-data.mojang.com/v1/objects/6bce4ef400e4efaa63a13d5e6f6b500be969ef81/server.jar)
  - [![](https://www.google.com/s2/favicons?size=64&domain=https://minecraft.net/)minecraft_server.1.21.9.jar](https://piston-data.mojang.com/v1/objects/11e54c2081420a4d49db3007e66c80a22579ff2a/server.jar)

</details>

## 概要

コンテナ型仮想環境で、Java版マインクラフトサーバーを構築します。  
使用するコンテナイメージは Docker 社が運営する公開レジストリの Docker Hub から取得します。  

| Service | Image |
|:-|:-|
| minecraft-core | [almalinux](https://hub.docker.com/_/almalinux)[:8](https://hub.docker.com/_/almalinux/tags?name=8) |
| minecraft-rcon | [almalinux](https://hub.docker.com/_/almalinux)[:8](https://hub.docker.com/_/almalinux/tags?name=8) |
| minecraft-rcon-web | [php](https://hub.docker.com/_/php)[:apache](https://hub.docker.com/_/php/tags?name=apache) |
| minecraft-database-admin | [phpmyadmin/phpmyadmin](https://hub.docker.com/_/phpmyadmin) |
| minecraft-database | [mysql](https://hub.docker.com/_/mysql) |

## コンテナ作成
1. 環境変数ファイル（ファイル名： `.env` ） を作成・編集する。（詳細は公式ドキュメントを参照）

```c:.env
minecraft_server_port=25565
```

## コンテナの生成と起動

```bash
docker compose up -d --build
```

> [!TIP]
> `docker compose logs` を実行して、`Done (*.***s)! For help, type "help"` が表示されれば起動完了。

## コンテナ停止

```bash
docker compose down
```

## コンテナ削除（ワールド初期化）

```bash
docker compose down --rmi all --volumes --remove-orphans
```

## Env

![version:1.21.8](https://img.shields.io/badge/version-1.21.8-brightgreen)

<details>

| name | default | remark |
| :- | :- | :- |
| minecraft_server_port | `25560-65530` | **コンテナ起動ごと**<br>Vender Preset: `25565` |
| minecraft_mod_dynmap_port | `25560-65530` | **コンテナ起動ごと**<br>Vender Preset: `8123` |
| minecraft_server_jar_url | `https://piston-data.mojang.com/v1/objects/6bce4ef400e4efaa63a13d5e6f6b500be969ef81/server.jar` | **初回起動時のみ** |
| minecraft_server_version | `1.21.8` | **初回起動時のみ** |
| minecraft_server_config_servericon | `https://n138-kz.github.io/Dockerfile.minecraft/assets/sample-server-icon.png` | **初回起動時のみ** |
| minecraft_server_config_difficulty | `normal` | **初回起動時のみ**<br>Syntax: `peaceful` \| `easy` \| `normal` \| `hard` |
| minecraft_server_config_enable_command_block | `false` | **初回起動時のみ**<br>Syntax: `true` \| `false` |
| minecraft_server_config_enable_jmx_monitoring | `false` | **初回起動時のみ**<br>Syntax: `true` \| `false` |
| minecraft_server_config_enable_query | `false` | **初回起動時のみ**<br>Syntax: `true` \| `false` |
| minecraft_server_config_enable_rcon | `true` | **初回起動時のみ**<br>Syntax: `true` \| `false` |
| minecraft_server_config_enable_status | `true` | **初回起動時のみ**<br>Syntax: `true` \| `false` |
| minecraft_server_config_enforce_secure_profile | `true` | **初回起動時のみ**<br>Syntax: `true` \| `false` |
| minecraft_server_config_enforce_whitelist | `false` | **初回起動時のみ**<br>Syntax: `true` \| `false` |
| minecraft_server_config_entity_broadcast_range_percentage | `100` | **初回起動時のみ** |
| minecraft_server_config_force_gamemode | `false` | **初回起動時のみ**<br>Syntax: `true` \| `false` |
| minecraft_server_config_function_permission_level | `2` | **初回起動時のみ** |
| minecraft_server_config_gamemode | `survival` | **初回起動時のみ** |
| minecraft_server_config_generate_structures | `true` | **初回起動時のみ**<br>Syntax: `true` \| `false` |
| minecraft_server_config_generator_settings | __not set__ | **初回起動時のみ** |
| minecraft_server_config_hardcore | `false` | **初回起動時のみ** |
| minecraft_server_config_hide_online_players | `false` | **初回起動時のみ** |
| minecraft_server_config_initial_disabled_packs | __not set__ | **初回起動時のみ** |
| minecraft_server_config_initial_enabled_packs | `vanilla` | **初回起動時のみ** |
| minecraft_server_config_level_name | `world` | **初回起動時のみ** |
| minecraft_server_config_level_seed | __not set__ | **初回起動時のみ** |
| minecraft_server_config_level_type | `minecraft\:normal` | **初回起動時のみ** |
| minecraft_server_config_log_ips | `true` | **初回起動時のみ** |
| minecraft_server_config_max_chained_neighbor_updates | `1000000` | **初回起動時のみ** |
| minecraft_server_config_max_players | `10` | **初回起動時のみ** |
| minecraft_server_config_max_tick_time | `60000` | **初回起動時のみ** |
| minecraft_server_config_max_world_size | 29999984 | **初回起動時のみ** |
| minecraft_server_config_motd | `Private server` | **初回起動時のみ** |
| minecraft_server_config_network_compression_threshold | `256` | **初回起動時のみ** |
| minecraft_server_config_online_mode | `true` | **初回起動時のみ** |
| minecraft_server_config_op_permission_level | `4` | **初回起動時のみ** |
| minecraft_server_config_pause_when_empty_seconds | `60` | **初回起動時のみ** |
| minecraft_server_config_player_idle_timeout | `0` | **初回起動時のみ** |
| minecraft_server_config_prevent_proxy_connections | `false` | **初回起動時のみ** |
| minecraft_server_config_pvp | `true` | **初回起動時のみ** |
| minecraft_server_config_query_port | `25565` | **初回起動時のみ** |
| minecraft_server_config_rate_limit | `0` | **初回起動時のみ** |
| minecraft_server_config_rcon_password | `25575password@1` | **初回起動時のみ** |
| minecraft_server_config_rcon_port | `25575` | **初回起動時のみ** |
| minecraft_server_config_region_file_compression | `deflate` | **初回起動時のみ** |
| minecraft_server_config_require_resource_pack | `false` | **初回起動時のみ** |
| minecraft_server_config_resource_pack | __not set__ | **初回起動時のみ** |
| minecraft_server_config_resource_pack_id | __not set__ | **初回起動時のみ** |
| minecraft_server_config_resource_pack_prompt | __not set__ | **初回起動時のみ** |
| minecraft_server_config_resource_pack_sha1 | __not set__ | **初回起動時のみ** |
| minecraft_server_config_server_ip | __not set__ | **初回起動時のみ** |
| minecraft_server_config_server_port | `25565` | **初回起動時のみ** |
| minecraft_server_config_simulation_distance | `10` | **初回起動時のみ** |
| minecraft_server_config_spawn_monsters | `true` |  **初回起動時のみ** |
| minecraft_server_config_spawn_protection | `16` |  **初回起動時のみ** |
| minecraft_server_config_sync_chunk_writes | `true` |  **初回起動時のみ** |
| minecraft_server_config_text_filtering_config | __not set__ | **初回起動時のみ** |
| minecraft_server_config_text_filtering_version | `0` | **初回起動時のみ** |
| minecraft_server_config_use_native_transport | `true` | **初回起動時のみ** |
| minecraft_server_config_view_distance | `10` | **初回起動時のみ** |
| minecraft_server_config_white_list | `false` | **初回起動時のみ** |

- `コンテナ起動ごと`: コンテナ停止→起動の度に設定されている内容を使用
- `初回起動時のみ`: コンテナビルド時のみ使用（運用中に変更する場合は`server.properties`を手動で変更）

</details>

## ワールド生成～op権限付与

```bash
# Compose Build
docker compose build --no-cache

# Compose up, Server up, World Generate
docker compose up -d

# Server up check
docker compose logs
```

```bash
# Check login user name
docker compose exec -it minecraft-rcon mcrcon list

# Give OP privilage
#  |  mojang <-- username
docker compose exec -it minecraft-rcon mcrcon "op mojang"
```

## fablic MOD server

### Server

- [Download Minecraft Server Launcher](https://fabricmc.net/use/server/)

> [!TIP]
> [curl -O, --remote-name オプション](https://github.com/wada811/blog/issues/29)  
> ファイルとして出力する。  
> URL のファイル名が出力するファイル名となる。  

> [!TIP]
> [curl -J, --remote-header-name オプション](https://github.com/wada811/blog/issues/29)  
> ファイルとして出力する。  
> ヘッダーの Content-Disposition のファイル名が出力するファイル名となる。  

<details>

```bash
# List files (before)
docker compose exec -it minecraft-core bash -c "ls -l"

# Downloads file
docker compose exec -it minecraft-core bash -c "curl -o server.jar https://meta.fabricmc.net/v2/versions/loader/1.21.8/0.17.2/1.1.0/server/jar"

# Downloads file (option)
docker compose exec -it minecraft-core bash -c "curl -OJ https://meta.fabricmc.net/v2/versions/loader/1.21.8/0.17.2/1.1.0/server/jar"

# List files (after)
docker compose exec -it minecraft-core bash -c "ls -l"

# Mods directory
docker compose exec -it minecraft-core bash -c "ls -l mods"
docker compose exec -it minecraft-core bash -c "rmdir /var/minecraft/mods"
mkdir mods && docker compose exec -it minecraft-core bash -c "ln -s /mnt/host/mods /var/minecraft"
docker compose exec -it minecraft-core bash -c "ls -l mods mods/"

# Restart server
docker compose exec -it minecraft-rcon mcrcon list "say Restarting server" "say サーバー再起動中" save-all stop
docker compose down
docker compose up -d
docker compose logs
```

</details>

### Client

- [Download Minecraft Client Launcher](https://fabricmc.net/use/installer/)




## アップグレード

1. 新しいバージョンの `server.jar` をコンテナ内にダウンロード(別名で保存して、コピーを `server.jar` に置換してください。)
2. コンテナ再起動

```bash
cd $(dirname $(docker compose ls | grep minecraft | awk '{print $3}'))
docker compose exec -it minecraft-core bash
wget -O minecraft_server.1.21.3.jar https://piston-data.mojang.com/v1/objects/45810d238246d90e811d896f87b14695b7fb6839/server.jar
mv minecraft_server.1.21.3.jar server.jar
exit # or [ctrl^D]
docker compose down; docker compose up -d
```
