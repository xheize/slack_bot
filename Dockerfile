FROM python:3.10.10-alpine3.17

WORKDIR /app

COPY . .

RUN pip install -r ./requirements.txt

CMD ["python","main.py"]