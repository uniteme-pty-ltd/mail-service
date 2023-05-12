FROM python:3-slim-bullseye
WORKDIR /app

LABEL maintainer="Toby Scott <hi@tobyscott.dev>"

RUN apt update
RUN apt install -y curl

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80
ENV FLASK_APP=wsgi.py

EXPOSE 80

CMD ["flask", "run"]
