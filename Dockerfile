FROM python:3.8

ARG DEBIAN_FRONTEND=noninteracive
RUN apt-get update -y && apt-get install -y python-pip python-dev
COPY . ./reuseapp
RUN python3.8 -m venv venv
RUN . venv/bin/activate
RUN pip install --upgrade pip
RUN apt install postgresql
RUN pip install -r requirements.txt
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD flask run --host=0.0.0.0 --port=${PORT:-5000}
