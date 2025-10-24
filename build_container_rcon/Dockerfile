FROM ubuntu:latest

ARG minecraft_server_config_rcon_host
ARG minecraft_server_config_rcon_port
ARG minecraft_server_config_rcon_password

RUN set -x && \
    apt-get update && apt-get upgrade -y

RUN set -x && \
    apt-get install -y wget git make gcc

WORKDIR /var/minecraft/

RUN set -x && \
    git clone https://github.com/Tiiffi/mcrcon.git

WORKDIR /var/minecraft/mcrcon/

RUN set -x && \
    make

RUN set -x && \
    make install

RUN set -x && \
    mcrcon -v

WORKDIR /var/minecraft/

ENV MCRCON_HOST=${minecraft_server_config_rcon_host}
ENV MCRCON_PORT=${minecraft_server_config_rcon_port}
ENV MCRCON_PASS=${minecraft_server_config_rcon_password}

RUN echo 'alias ll="ls -l"' >> /etc/bashrc
RUN echo '' >> /etc/bashrc
RUN echo 'mcrcon -h' >> /etc/bashrc

ENTRYPOINT ["sh"]
