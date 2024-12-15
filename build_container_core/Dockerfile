FROM almalinux:8
USER root:root

ARG minecraft_server_jar_url
ARG minecraft_server_version

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
RUN echo 'difficulty=normal' >> server.properties
RUN echo 'max-players=10' >> server.properties
RUN echo 'motd=Private server' >> server.properties
RUN echo 'enable-rcon=true' >> server.properties
RUN echo 'rcon.password=25575password@1' >> server.properties
#RUN echo 'gamemode=creative' >> server.properties
#RUN echo 'level-type=FLAT' >> server.properties
#RUN echo 'minecraft:bedrock,3*minecraft:stone,52*minecraft:sandstone;' > level.dat

ENTRYPOINT [ "java","-Xms512m","-Xmx2048m","-jar","server.jar","nogui" ]
