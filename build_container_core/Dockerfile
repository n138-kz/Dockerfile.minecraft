FROM almalinux:8
USER root:root

ARG minecraft_server_jar_url
ARG minecraft_server_version
ARG minecraft_server_config_difficulty
ARG minecraft_server_config_enable-command-block
ARG minecraft_server_config_enable-jmx-monitoring
ARG minecraft_server_config_enable-query
ARG minecraft_server_config_enable-rcon
ARG minecraft_server_config_max-players
ARG minecraft_server_config_motd
ARG minecraft_server_config_enable-status
ARG minecraft_server_config_enforce-secure-profile
ARG minecraft_server_config_enforce-whitelist
ARG minecraft_server_config_entity-broadcast-range-percentage
ARG minecraft_server_config_force-gamemode
ARG minecraft_server_config_function-permission-level
ARG minecraft_server_config_gamemode
ARG minecraft_server_config_generate-structures
ARG minecraft_server_config_generator-settings
ARG minecraft_server_config_hardcore
ARG minecraft_server_config_hide-online-players
ARG minecraft_server_config_initial-disabled-packs
ARG minecraft_server_config_initial-enabled-packs
ARG minecraft_server_config_level-name
ARG minecraft_server_config_level-seed
ARG minecraft_server_config_level-type
ARG minecraft_server_config_log-ips
ARG minecraft_server_config_max-chained-neighbor-updates
ARG minecraft_server_config_max-tick-time
ARG minecraft_server_config_max-world-size
ARG minecraft_server_config_network-compression-threshold
ARG minecraft_server_config_online-mode
ARG minecraft_server_config_op-permission-level
ARG minecraft_server_config_pause-when-empty-seconds
ARG minecraft_server_config_player-idle-timeout
ARG minecraft_server_config_rcon-password

RUN set -x && \
    dnf update -y --security

RUN set -x && \
    dnf install -y curl

RUN set -x && \
    dnf install -y wget

RUN set -x && \
    dnf install -y java-21-openjdk-headless

WORKDIR /var/minecraft/

RUN set -x && \
    wget ${minecraft_server_jar_url} -O minecraft_server.${minecraft_server_version}.jar

RUN set -x && \
    cp minecraft_server.${minecraft_server_version}.jar server.jar

RUN echo '# '$(date) > eula.txt
RUN echo 'eula=true' >> eula.txt

RUN echo '#Minecraft server properties' > server.properties
RUN echo "difficulty=${minecraft_server_config_difficulty}" >> server.properties
RUN echo "enable-command-block=${minecraft_server_config_enable-command-block}" >> server.properties
RUN echo "enable-jmx-monitoring=${minecraft_server_config_enable-jmx-monitoring}" >> server.properties
RUN echo "enable-query=${minecraft_server_config_enable-query}" >> server.properties
RUN echo "enable-rcon=${minecraft_server_config_enable-rcon}" >> server.properties
RUN echo "max-players=${minecraft_server_config_max-players}" >> server.properties
RUN echo "motd=${minecraft_server_config_motd}" >> server.properties
RUN echo "enable-status=${minecraft_server_config_enable-status}" >> server.properties
RUN echo "enforce-secure-profile=${minecraft_server_config_enforce-secure-profile}" >> server.properties
RUN echo "enforce-whitelist=${minecraft_server_config_enforce-whitelist}" >> server.properties
RUN echo "entity-broadcast-range-percentage=${minecraft_server_config_entity-broadcast-range-percentage}" >> server.properties
RUN echo "force-gamemode=${minecraft_server_config_force-gamemode}" >> server.properties
RUN echo "function-permission-level=${minecraft_server_config_function-permission-level}" >> server.properties
RUN echo "gamemode=${minecraft_server_config_gamemode}" >> server.properties
RUN echo "generate-structures=${minecraft_server_config_generate-structures}" >> server.properties
RUN echo "generator-settings=${minecraft_server_config_generator-settings}" >> server.properties
RUN echo "hardcore=${minecraft_server_config_hardcore}" >> server.properties
RUN echo "hide-online-players=${minecraft_server_config_hide-online-players}" >> server.properties
RUN echo "initial-disabled-packs=${minecraft_server_config_initial-disabled-packs}" >> server.properties
RUN echo "initial-enabled-packs=${minecraft_server_config_initial-enabled-packs}" >> server.properties
RUN echo "level-name=${minecraft_server_config_level-name}" >> server.properties
RUN echo "level-seed=${minecraft_server_config_level-seed}" >> server.properties
RUN echo "level-type=${minecraft_server_config_level-type}" >> server.properties
RUN echo "log-ips=${minecraft_server_config_log-ips}" >> server.properties
RUN echo "max-chained-neighbor-updates=${minecraft_server_config_max-chained-neighbor-updates}" >> server.properties
RUN echo "max-tick-time=${minecraft_server_config_max-tick-time}" >> server.properties
RUN echo "max-world-size=${minecraft_server_config_max-world-size}" >> server.properties
RUN echo "network-compression-threshold=${minecraft_server_config_network-compression-threshold}" >> server.properties
RUN echo "online-mode=${minecraft_server_config_online-mode}" >> server.properties
RUN echo "op-permission-level=${minecraft_server_config_op-permission-level}" >> server.properties
RUN echo "pause-when-empty-seconds=${minecraft_server_config_pause-when-empty-seconds}" >> server.properties
RUN echo "player-idle-timeout=${minecraft_server_config_player-idle-timeout}" >> server.properties
RUN echo "rcon.password=${minecraft_server_config_rcon-password}" >> server.properties
#RUN echo 'gamemode=creative' >> server.properties
#RUN echo 'level-type=FLAT' >> server.properties
#RUN echo 'minecraft:bedrock,3*minecraft:stone,52*minecraft:sandstone;' > level.dat

ENTRYPOINT [ "java","-Xms512m","-Xmx2048m","-jar","server.jar","nogui" ]
