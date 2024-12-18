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
RUN echo 'rcon.password=25575password@1' >> server.properties
#RUN echo 'gamemode=creative' >> server.properties
#RUN echo 'level-type=FLAT' >> server.properties
#RUN echo 'minecraft:bedrock,3*minecraft:stone,52*minecraft:sandstone;' > level.dat

ENTRYPOINT [ "java","-Xms512m","-Xmx2048m","-jar","server.jar","nogui" ]
