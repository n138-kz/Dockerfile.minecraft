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
- [mcrcon](https://github.com/Tiiffi/mcrcon.git)
- [MinecraftのサーバにRCONで接続する | Qiita](https://qiita.com/h_tyokinuhata/items/85d855f88d5d33c21949)

<details>

  <summary>Minecraft Server Each Versions</summary>

  - [![](https://www.google.com/s2/favicons?size=64&domain=https://minecraft.net/)minecraft_server.1.21.1.jar](https://piston-data.mojang.com/v1/objects/59353fb40c36d304f2035d51e7d6e6baa98dc05c/server.jar)
  - [![](https://www.google.com/s2/favicons?size=64&domain=https://minecraft.net/)minecraft_server.1.21.3.jar](https://piston-data.mojang.com/v1/objects/45810d238246d90e811d896f87b14695b7fb6839/server.jar)
  - [![](https://www.google.com/s2/favicons?size=64&domain=https://minecraft.net/)minecraft_server.1.21.8.jar](https://piston-data.mojang.com/v1/objects/6bce4ef400e4efaa63a13d5e6f6b500be969ef81/server.jar)

</details>



## Env

![version:1.21.8](https://img.shields.io/badge/version-1.21.8-brightgreen)

| name | default | remark |
| :- | :- | :- |
| minecraft_server_port | 25560-65530 | :25565 |
| minecraft_mod_dynmap_port | 25560-65530 | :8123 |
| minecraft_server_jar_url | https://piston-data.mojang.com/v1/objects/6bce4ef400e4efaa63a13d5e6f6b500be969ef81/server.jar | |
| minecraft_server_version | 1.21.8 | |
| minecraft_server_config_servericon | https://n138-kz.github.io/Dockerfile.minecraft/assets/sample-server-icon.png | |
| minecraft_server_config_difficulty | normal | |
| minecraft_server_config_enable_command_block | false | |
| minecraft_server_config_enable_jmx_monitoring | false | |
| minecraft_server_config_enable_query | false | |
| minecraft_server_config_enable_rcon | true | |
| minecraft_server_config_enable_status | true | |
| minecraft_server_config_enforce_secure_profile | true | |
| minecraft_server_config_enforce_whitelist | false | |
| minecraft_server_config_entity_broadcast_range_percentage | 100 | |
| minecraft_server_config_force_gamemode | false | |
| minecraft_server_config_function_permission_level | 2 | |
| minecraft_server_config_gamemode | survival | |
| minecraft_server_config_generate_structures | true | |
| minecraft_server_config_generator_settings | { | | | |
| minecraft_server_config_hardcore | false | |
| minecraft_server_config_hide_online_players | false | |
| minecraft_server_config_initial_disabled_packs |  | |
| minecraft_server_config_initial_enabled_packs | vanilla | |
| minecraft_server_config_level_name | world | |
| minecraft_server_config_level_seed |  | |
| minecraft_server_config_level_type | minecraft\:normal | |
| minecraft_server_config_log_ips | true | |
| minecraft_server_config_max_chained_neighbor_updates | 1000000 | |
| minecraft_server_config_max_players | 10 | |
| minecraft_server_config_max_tick_time | 60000 | |
| minecraft_server_config_max_world_size | 29999984 | |
| minecraft_server_config_motd | Private server | |
| minecraft_server_config_network_compression_threshold | 256 | |
| minecraft_server_config_online_mode | true | |
| minecraft_server_config_op_permission_level | 4 | |
| minecraft_server_config_pause_when_empty_seconds | 60 | |
| minecraft_server_config_player_idle_timeout | 0 | |
| minecraft_server_config_prevent_proxy_connections | false | |
| minecraft_server_config_pvp | true | |
| minecraft_server_config_query_port | 25565 | |
| minecraft_server_config_rate_limit | 0 | |
| minecraft_server_config_rcon_password | 25575password@1 | |
| minecraft_server_config_rcon_port | 25575 | |
| minecraft_server_config_region_file_compression | deflate | |
| minecraft_server_config_require_resource_pack | false | |
| minecraft_server_config_resource_pack |  | |
| minecraft_server_config_resource_pack_id |  | |
| minecraft_server_config_resource_pack_prompt |  | |
| minecraft_server_config_resource_pack_sha1 |  | |
| minecraft_server_config_server_ip |  | |
| minecraft_server_config_server_port | 25565 | |
| minecraft_server_config_simulation_distance | 10 | |
| minecraft_server_config_spawn_monsters | true | |
| minecraft_server_config_spawn_protection | 16 | |
| minecraft_server_config_sync_chunk_writes | true | |
| minecraft_server_config_text_filtering_config |  | |
| minecraft_server_config_text_filtering_version | 0 | |
| minecraft_server_config_use_native_transport | true | |
| minecraft_server_config_view_distance | 10 | |
| minecraft_server_config_white_list | false | |

## 概要

コンテナ型仮想環境で、Java版マインクラフトサーバーを構築します。  
使用するコンテナイメージは Docker 社が運営する公開レジストリの Docker Hub から取得します。  

## コンテナ作成
1. 環境変数ファイル（ファイル名： `.env` ） を作成・編集する。（詳細は公式ドキュメントを参照）

```c:.env
minecraft_server_jar_url="https://piston-data.mojang.com/v1/objects/45810d238246d90e811d896f87b14695b7fb6839/server.jar"
minecraft_server_version="1.21.3"
```

## コンテナの生成と起動

```bash
docker compose up -d --build
```

> [!TIP]
> `docker compose logs -f` を実行して、`Done (*.***s)! For help, type "help"` が表示されれば起動完了。

## コンテナ停止

```bash
docker compose down
```

## コンテナ削除（ワールド初期化）

```bash
docker compose down --rmi all --volumes --remove-orphans
```


