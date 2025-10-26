FROM python:latest

ARG minecraft_server_config_rcon_host
ARG minecraft_server_config_rcon_port
ARG minecraft_server_config_rcon_password
COPY requirements.txt /var/minecraft/
COPY bot.py /var/minecraft/

WORKDIR /var/minecraft/

RUN set -x && \
    pip install -r requirements.txt

ENV MCRCON_HOST=${minecraft_server_config_rcon_host}
ENV MCRCON_PORT=${minecraft_server_config_rcon_port}
ENV MCRCON_PASS=${minecraft_server_config_rcon_password}

ENTRYPOINT ["python3", "bot.py"]
