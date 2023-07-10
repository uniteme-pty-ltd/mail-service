FROM alpine:3.18.2 as release
WORKDIR /app

LABEL maintainer="Toby Scott <hi@tobyscott.dev>"

RUN apk update
RUN apk upgrade
RUN apk add --no-cache ca-certificates
RUN apk add --no-cache curl
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80
ENV FLASK_APP=wsgi.py

EXPOSE 80

CMD ["flask", "run"]
