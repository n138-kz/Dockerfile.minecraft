FROM alpine:latest
WORKDIR /minecraft
RUN apk add --no-cache openjdk25 curl wget && wget -O minecraft_server.26.2.jar https://piston-data.mojang.com/v1/objects/823e2250d24b3ddac457a60c92a6a941943fcd6a/server.jar && ln -s minecraft_server.26.2.jar server.jar && java -jar server.jar && sed -i -e 's/eula=false/eula=true/g' eula.txt
RUN echo '#!/bin/sh' > /usr/local/bin/ll && echo 'ls -lh' >> /usr/local/bin/ll && chmod a+x /usr/local/bin/ll

ENTRYPOINT [ "java","-Xms512m","-Xmx2048m","-jar","server.jar","nogui" ]
