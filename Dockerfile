FROM python:3.11.2-alpine3.17
WORKDIR /app

LABEL maintainer="Toby Scott <hi@tobyscott.dev>"

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80
ENV FLASK_APP=wsgi.py

EXPOSE 80

CMD ["flask", "run"]
