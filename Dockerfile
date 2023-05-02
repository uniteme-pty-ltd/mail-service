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

HEALTHCHECK --interval=3s --timeout=3s --start-period=10s --retries=5 CMD [ "curl -f http://127.0.0.1/health || exit 1" ]
# HEALTHCHECK NONE

CMD ["flask", "run"]
