FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

#RUN apt-get update \
#    && apt-get install gcc -y \
#    && apt-get clean

RUN export PYTHONPATH=$PWD

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /app/

#CMD gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000