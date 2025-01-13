FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip &&  pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENV TWITCH_API_TOKEN=$TWITCH_API_TOKEN
ENV TWITCH_INITIAL_CHANNELS=$TWITCH_INITIAL_CHANNELS

RUN python3 twitchbot/app.py
