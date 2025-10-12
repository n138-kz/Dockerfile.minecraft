FROM ubuntu
USER root:root

RUN apt-get update && \
    apt-get -y upgrade

RUN apt-get install -y cron

RUN mountpoint -q /var/minecraft/ || exit 1

WORKDIR /var/minecraft/
