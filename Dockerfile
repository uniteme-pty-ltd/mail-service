FROM python:3.11.2-alpine3.17

LABEL maintainer="Toby Scott <hi@tobyscott.dev>"

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV FLASK_APP=wsgi.py

EXPOSE 5000

CMD ["flask", "run"]
