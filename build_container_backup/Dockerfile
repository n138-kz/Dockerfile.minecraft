FROM ubuntu:latest

ARG minecraft_server_config_rcon_host
ARG minecraft_server_config_rcon_port
ARG minecraft_server_config_rcon_password

RUN set -x && \
    apt-get update

RUN set -x && \
    apt-get install -y cron
