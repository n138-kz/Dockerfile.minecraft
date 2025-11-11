FROM python:3.14

COPY .env /media/
COPY minecraft-discordapp1/requirements.txt /media/
RUN python3 -m pip install --upgrade pip
RUN pip install -r /media/requirements.txt

WORKDIR /media
ENTRYPOINT ["python3", "/media/main.py"]
