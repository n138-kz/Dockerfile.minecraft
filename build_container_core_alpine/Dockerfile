FROM alpine:latest
ARG PLAIN_RCON_PASSWORD=${PLAIN_RCON_PASSWORD:-}
ARG PLAIN_RCON_PORT=${PLAIN_RCON_PORT:-25575}
WORKDIR /minecraft
RUN apk add --no-cache openjdk25 curl wget && wget -O minecraft_server.26.2.jar https://piston-data.mojang.com/v1/objects/823e2250d24b3ddac457a60c92a6a941943fcd6a/server.jar && ln -s minecraft_server.26.2.jar server.jar && java -jar server.jar && sed -i -e 's/eula=false/eula=true/g' eula.txt
RUN sed -i -e 's/enable-rcon=false/enable-rcon=true/g' server.properties || true; sed -i -e "s/rcon.password=/rcon.password=${PLAIN_RCON_PASSWORD}" server.properties || true; sed -i -e "s/rcon.port=25575/rcon.port=${PLAIN_RCON_PORT}" server.properties || true
RUN echo '#!/bin/sh' > /usr/local/bin/ll && echo 'ls -lh' >> /usr/local/bin/ll && chmod a+x /usr/local/bin/ll
