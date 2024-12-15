# README

## 概要

![version:1.21.1](https://img.shields.io/badge/version-1.21.1-brightgreen)

コンテナ型仮想環境で、Java版マインクラフトサーバーを構築します。  
使用するコンテナイメージは Docker 社が運営する公開レジストリの Docker Hub から取得します。  

> [!TIP]
> MODサーバでは無く公式配布サーバアプリケーションを使用しますが、[MODサーバ（i.e. Fabric）](#fablic-mod-server)を使用する場合は、[後述環境変数ファイル](#コンテナ作成)を適宜修正してから `build` してください。
> -> コンテナ作成 > No.3

## 事前準備

デバイスやソフトウェアは以下を用いる。  

- サーバ機（Ubuntu Server、Docker）
- Docker Hub
	- [almalinux:8](https://hub.docker.com/_/almalinux)

1. Docker のインストール
    
	[インストール方法](https://docs.docker.jp/engine/installation/linux/index.html)  

	<details>
		<summary>Tips for collapsed sections</summary>

	</details>

3. データ格納用ディレクトリの用意

> [!IMPORTANT]
> 以降のコマンド操作は設定したディレクトリで行うものとする。

## コンテナ作成

1. Compose ファイル を編集する。（詳細は[公式ドキュメント](https://docker-minecraft-server.readthedocs.io/en/latest/variables/)を参照）

```bash
git clone https://github.com/n138-kz/Dockerfile.git
cd Dockerfile/n138-kz/minecraft1.21.1/
```

2. 環境変数ファイル（ファイル名： `.env` ） を作成・編集する。（詳細は公式ドキュメントを参照）

```c:.env
minecraft_server_jar_url="https://piston-data.mojang.com/v1/objects/59353fb40c36d304f2035d51e7d6e6baa98dc05c/server.jar"
minecraft_server_version="1.21.1"
```

3. 必要に応じて、個別設定を [Dockerfile ファイル](./build_container_core/Dockerfile) に記載する。

例
```diff
- #RUN echo 'gamemode=creative' >> server.properties
- #RUN echo 'level-type=FLAT' >> server.properties
- #RUN echo 'minecraft:bedrock,3*minecraft:stone,52*minecraft:sandstone;' > level.dat
+ RUN echo 'gamemode=creative' >> server.properties
+ RUN echo 'level-type=FLAT' >> server.properties
+ RUN echo 'minecraft:bedrock,3*minecraft:stone,52*minecraft:sandstone;' > level.dat
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

> [!IMPORTANT]
> ワールドデータは永続保持される設定のため、サーバ再構築などデータをすべて初期化する場合は、`docker compose down --rmi all --volumes --remove-orphans` を実行する。

> [!CAUTION]
> `docker compose down --rmi all --volumes --remove-orphans` はワールドデータも削除するため、取り扱いには十分注意すること。

## fablic MOD server

```bash
docker compose exec -it minecraft-core bash
cd mods/
curl -o 'fabric-api.jar' https://www.curseforge.com/api/v1/mods/306612/files/5750140/download
exit
docker compose down
docker compose up -d
```

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

## 参考

### docker-compose

- [《滅びの呪文》Docker Composeで作ったコンテナ、イメージ、ボリューム、ネットワークを一括完全消去する便利コマンド](https://qiita.com/suin/items/19d65e191b96a0079417)

### Github/README

- [GitHubでQiitaの:::noteみたいな強調をする](https://qiita.com/lobmto/items/d02532134782f34c0e2fs)

### minecraft-core

- [Java 版 Minecraft サーバー](https://www.minecraft.net/ja-jp/download/server)

	<details>		
	<summary>each versions</summary>
	
	- [minecraft_server.1.21.1.jar](https://piston-data.mojang.com/v1/objects/59353fb40c36d304f2035d51e7d6e6baa98dc05c/server.jar)
	- [minecraft_server.1.21.3.jar](https://piston-data.mojang.com/v1/objects/45810d238246d90e811d896f87b14695b7fb6839/server.jar)

	</details>

- [Fabric Minecraft Server](https://fabricmc.net/use/server/)

### minecraft-rcon

- [mcrcon](https://github.com/Tiiffi/mcrcon.git)
- [MinecraftのサーバにRCONで接続する | Qiita](https://qiita.com/h_tyokinuhata/items/85d855f88d5d33c21949)
