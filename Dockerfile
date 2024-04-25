FROM python:3.10.11-alpine3.17
LABEL "heart.beat.url"="http://slack-bot:8000/api/v1/heart-beat"

WORKDIR /app

COPY . .

RUN pip install -r ./requirements.txt

CMD ["python","main.py"]