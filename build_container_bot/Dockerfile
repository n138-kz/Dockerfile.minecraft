FROM python:latest

ARG minecraft_server_config_rcon_host
ARG minecraft_server_config_rcon_port
ARG minecraft_server_config_rcon_password

RUN set -x && \
    pip install -r requirements.txt

WORKDIR /var/minecraft/

ENV MCRCON_HOST=${minecraft_server_config_rcon_host}
ENV MCRCON_PORT=${minecraft_server_config_rcon_port}
ENV MCRCON_PASS=${minecraft_server_config_rcon_password}

ENTRYPOINT ["python3", "bot.py"]
