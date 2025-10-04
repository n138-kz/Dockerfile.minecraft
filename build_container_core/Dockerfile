FROM almalinux:8
USER root:root

ARG minecraft_server_jar_url
ARG minecraft_server_version
ARG minecraft_server_java_xmx
ARG minecraft_server_java_xms
ARG minecraft_server_config_servericon
ARG minecraft_server_config_difficulty
ARG minecraft_server_config_enable_command_block
ARG minecraft_server_config_enable_jmx_monitoring
ARG minecraft_server_config_enable_query
ARG minecraft_server_config_enable_rcon
ARG minecraft_server_config_enable_status
ARG minecraft_server_config_enforce_secure_profile
ARG minecraft_server_config_enforce_whitelist
ARG minecraft_server_config_entity_broadcast_range_percentage
ARG minecraft_server_config_force_gamemode
ARG minecraft_server_config_function_permission_level
ARG minecraft_server_config_gamemode
ARG minecraft_server_config_generate_structures
ARG minecraft_server_config_generator_settings
ARG minecraft_server_config_hardcore
ARG minecraft_server_config_hide_online_players
ARG minecraft_server_config_initial_disabled_packs
ARG minecraft_server_config_initial_enabled_packs
ARG minecraft_server_config_level_name
ARG minecraft_server_config_level_seed
ARG minecraft_server_config_level_type
ARG minecraft_server_config_log_ips
ARG minecraft_server_config_max_chained_neighbor_updates
ARG minecraft_server_config_max_players
ARG minecraft_server_config_max_tick_time
ARG minecraft_server_config_max_world_size
ARG minecraft_server_config_motd
ARG minecraft_server_config_network_compression_threshold
ARG minecraft_server_config_online_mode
ARG minecraft_server_config_op_permission_level
ARG minecraft_server_config_pause_when_empty_seconds
ARG minecraft_server_config_player_idle_timeout
ARG minecraft_server_config_prevent_proxy_connections
ARG minecraft_server_config_pvp
ARG minecraft_server_config_query_port
ARG minecraft_server_config_rate_limit
ARG minecraft_server_config_rcon_password
ARG minecraft_server_config_rcon_port
ARG minecraft_server_config_region_file_compression
ARG minecraft_server_config_require_resource_pack
ARG minecraft_server_config_resource_pack
ARG minecraft_server_config_resource_pack_id
ARG minecraft_server_config_resource_pack_prompt
ARG minecraft_server_config_resource_pack_sha1
ARG minecraft_server_config_server_ip
ARG minecraft_server_config_server_port
ARG minecraft_server_config_simulation_distance
ARG minecraft_server_config_spawn_monsters
ARG minecraft_server_config_spawn_protection
ARG minecraft_server_config_sync_chunk_writes
ARG minecraft_server_config_text_filtering_config
ARG minecraft_server_config_text_filtering_version
ARG minecraft_server_config_use_native_transport
ARG minecraft_server_config_view_distance
ARG minecraft_server_config_white_list

RUN set -x && \
    dnf update -y --security

RUN set -x && \
    dnf install -y curl

RUN set -x && \
    dnf install -y wget

RUN set -x && \
    dnf install -y java-21-openjdk-headless

RUN set -x && \
    echo '#!/bin/bash' > /usr/local/bin/ll && \
    echo 'ls -l' >> /usr/local/bin/ll && \
    chmod a+x /usr/local/bin/ll

WORKDIR /var/minecraft/

RUN set -x && \
    wget ${minecraft_server_jar_url} -O minecraft_server.${minecraft_server_version}.jar

RUN set -x && \
    cp minecraft_server.${minecraft_server_version}.jar server.jar

RUN set -x && \
    wget ${minecraft_server_config_servericon} -O server-icon.png

RUN echo '# '$(date) > eula.txt
RUN echo 'eula=true' >> eula.txt

RUN echo '#Minecraft server properties' > server.properties.conf
RUN echo "difficulty=${minecraft_server_config_difficulty}" >> server.properties.conf
RUN echo "enable-command-block=${minecraft_server_config_enable_command_block}" >> server.properties.conf
RUN echo "enable-jmx-monitoring=${minecraft_server_config_enable_jmx_monitoring}" >> server.properties.conf
RUN echo "enable-query=${minecraft_server_config_enable_query}" >> server.properties.conf
RUN echo "enable-rcon=${minecraft_server_config_enable_rcon}" >> server.properties.conf
RUN echo "enable-status=${minecraft_server_config_enable_status}" >> server.properties.conf
RUN echo "enforce-secure-profile=${minecraft_server_config_enforce_secure_profile}" >> server.properties.conf
RUN echo "enforce-whitelist=${minecraft_server_config_enforce_whitelist}" >> server.properties.conf
RUN echo "entity-broadcast-range-percentage=${minecraft_server_config_entity_broadcast_range_percentage}" >> server.properties.conf
RUN echo "force-gamemode=${minecraft_server_config_force_gamemode}" >> server.properties.conf
RUN echo "function-permission-level=${minecraft_server_config_function_permission_level}" >> server.properties.conf
RUN echo "gamemode=${minecraft_server_config_gamemode}" >> server.properties.conf
RUN echo "generate-structures=${minecraft_server_config_generate_structures}" >> server.properties.conf
RUN echo "generator-settings=${minecraft_server_config_generator_settings}" >> server.properties.conf
RUN echo "hardcore=${minecraft_server_config_hardcore}" >> server.properties.conf
RUN echo "hide-online-players=${minecraft_server_config_hide_online_players}" >> server.properties.conf
RUN echo "initial-disabled-packs=${minecraft_server_config_initial_disabled_packs}" >> server.properties.conf
RUN echo "initial-enabled-packs=${minecraft_server_config_initial_enabled_packs}" >> server.properties.conf
RUN echo "level-name=${minecraft_server_config_level_name}" >> server.properties.conf
RUN echo "level-seed=${minecraft_server_config_level_seed}" >> server.properties.conf
RUN echo "level-type=${minecraft_server_config_level_type}" >> server.properties.conf
RUN echo "log-ips=${minecraft_server_config_log_ips}" >> server.properties.conf
RUN echo "max-chained-neighbor-updates=${minecraft_server_config_max_chained_neighbor_updates}" >> server.properties.conf
RUN echo "max-players=${minecraft_server_config_max_players}" >> server.properties.conf
RUN echo "max-tick-time=${minecraft_server_config_max_tick_time}" >> server.properties.conf
RUN echo "max-world-size=${minecraft_server_config_max_world_size}" >> server.properties.conf
RUN echo "motd=${minecraft_server_config_motd}" >> server.properties.conf
RUN echo "network-compression-threshold=${minecraft_server_config_network_compression_threshold}" >> server.properties.conf
RUN echo "online-mode=${minecraft_server_config_online_mode}" >> server.properties.conf
RUN echo "op-permission-level=${minecraft_server_config_op_permission_level}" >> server.properties.conf
RUN echo "pause-when-empty-seconds=${minecraft_server_config_pause_when_empty_seconds}" >> server.properties.conf
RUN echo "player-idle-timeout=${minecraft_server_config_player_idle_timeout}" >> server.properties.conf
RUN echo "prevent-proxy-connections=${minecraft_server_config_prevent_proxy_connections}" >> server.properties.conf
RUN echo "pvp=${minecraft_server_config_pvp}" >> server.properties.conf
RUN echo "query.port=${minecraft_server_config_query_port}" >> server.properties.conf
RUN echo "rate-limit=${minecraft_server_config_rate_limit}" >> server.properties.conf
RUN echo "rcon.password=${minecraft_server_config_rcon_password}" >> server.properties.conf
RUN echo "rcon.port=${minecraft_server_config_rcon_port}" >> server.properties.conf
RUN echo "region-file-compression=${minecraft_server_config_region_file_compression}" >> server.properties.conf
RUN echo "require-resource-pack=${minecraft_server_config_require_resource_pack}" >> server.properties.conf
RUN echo "resource-pack-id=${minecraft_server_config_resource_pack_id}" >> server.properties.conf
RUN echo "resource-pack-prompt=${minecraft_server_config_resource_pack_prompt}" >> server.properties.conf
RUN echo "resource-pack-sha1=${minecraft_server_config_resource_pack_sha1}" >> server.properties.conf
RUN echo "resource-pack=${minecraft_server_config_resource_pack}" >> server.properties.conf
RUN echo "server-ip=${minecraft_server_config_server_ip}" >> server.properties.conf
RUN echo "server-port=${minecraft_server_config_server_port}" >> server.properties.conf
RUN echo "simulation-distance=${minecraft_server_config_simulation_distance}" >> server.properties.conf
RUN echo "spawn-monsters=${minecraft_server_config_spawn_monsters}" >> server.properties.conf
RUN echo "spawn-protection=${minecraft_server_config_spawn_protection}" >> server.properties.conf
RUN echo "sync-chunk-writes=${minecraft_server_config_sync_chunk_writes}" >> server.properties.conf
RUN echo "text-filtering-config=${minecraft_server_config_text_filtering_config}" >> server.properties.conf
RUN echo "text-filtering-version=${minecraft_server_config_text_filtering_version}" >> server.properties.conf
RUN echo "use-native-transport=${minecraft_server_config_use_native_transport}" >> server.properties.conf
RUN echo "view-distance=${minecraft_server_config_view_distance}" >> server.properties.conf
RUN echo "white-list=${minecraft_server_config_white_list}" >> server.properties.conf
#RUN echo 'gamemode=creative' >> server.properties.conf
#RUN echo 'level-type=FLAT' >> server.properties.conf
#RUN echo 'minecraft:bedrock,3*minecraft:stone,52*minecraft:sandstone;' > level.dat

RUN set -x && if [ ! -s server.properties ] ; then cp server.properties.conf server.properties; fi
RUN set -x && rm server.properties.conf

RUN set -x && cat server.properties

ENTRYPOINT [ "java","-Xms${minecraft_server_java_xms}","-Xmx${minecraft_server_java_xmx}","-jar","server.jar","nogui" ]
