FROM python:3.14
WORKDIR /tmp

COPY .env /media/
COPY minecraft-discordapp1/requirements.txt /media/
RUN python3 -m pip install --upgrade pip
RUN pip install -r /media/requirements.txt

ENTRYPOINT ["python3", "/media/main.py"]
